import re
import io

from collections import Counter
from string import punctuation

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class WaitForElements(object):
    def __init__(self, locator, count):
        self.locator = locator
        self.count = count

    def __call__(self, driver):
        try:
            elements = EC._find_elements(driver, self.locator)
            return len(elements) > self.count
        except StaleElementReferenceException:
            return False


def empty(file_name):
    with open(file_name, "w"):
        pass


def init_driver():

    # initiate the driver:
    chromedriver = webdriver.Chrome("chromedriver")

    # set a default wait time for the browser [5 seconds here]:
    chromedriver.wait = WebDriverWait(chromedriver, 5)

    return chromedriver


def login_twitter(driver, username, password):
    # open the web page in the browser:
    try:
        driver.set_page_load_timeout(10)
        driver.get("https://twitter.com/login")
    except TimeoutException as ex:
        print(ex)
        driver.quit()
    except NoSuchWindowException as ex2:
        print(ex2)
        driver.quit()

    # initial wait for the page to load
    wait = WebDriverWait(driver, 5)

    # wait until the page is loaded:
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "js-password-field")))

    # find the boxes for username and password
    username_field = driver.find_element_by_class_name("js-username-field")
    password_field = driver.find_element_by_class_name("js-password-field")

    # enter your username:
    username_field.send_keys(username)

    # enter your password:
    password_field.send_keys(password)

    # click the "Log In" button:
    driver.find_element_by_class_name("EdgeButtom--medium").click()

    return


def last_n_tweets(driver, url, n):
    # open the web page in the browser, catch exceptions:
    try:
        driver.set_page_load_timeout(10)
        driver.get(url)
    # catch exceptions:
    except TimeoutException as ex:
        print(ex)
        driver.quit()
    except NoSuchWindowException as ex2:
        print(ex2)
        driver.quit()

    # the selector for a tweet's text:
    css_selector = ".js-tweet-text-container"

    # initial wait for the page to load
    wait = WebDriverWait(driver, 10)

    try:
        # wait until the first tweet is loaded:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))

        # initiate tweets counter:
        number_of_tweets = 0

        # scroll down until there are at least n visible tweets:
        while number_of_tweets < n:

            # extract all the tweets:
            tweets_list = driver.find_elements_by_css_selector(css_selector)

            # remove any empty tweets (for example: retweets with no text):
            for t in tweets_list:
                if t.text == "" or t.text == " " or not t.text:
                    tweets_list.remove(t)

            # find number of visible tweets:
            number_of_tweets = len(tweets_list)

            # keep scrolling:
            driver.execute_script("arguments[0].scrollIntoView();", tweets_list[-1])

            try:
                # wait for more tweets to be visible:
                wait.until(WaitForElements(
                    (By.CSS_SELECTOR, css_selector), number_of_tweets))

            except TimeoutException:
                # if no more are visible the "wait.until" call will timeout. Catch the exception and exit the while loop:
                break

            except NoSuchElementException:
                # if there are no elements with class="tweet-text" catch the exception and exit the while loop:
                break

        # put only the first n tweets in 'tweetsStr':
        tweets_list = tweets_list[0:n]
        tweets_list = [str(tweets_list.index(tweet) + 1) + '. ' + tweet.text for tweet in tweets_list]
        tweets_str = '\n\n'.join(t for t in tweets_list)

    except TimeoutException:

        # if there are no tweets then the "wait.until" call in the first "try" statement will time out.
        # So catch that exception and return an empty string.
        tweets_str = ""

    return tweets_str


def main(username, password, account_url, num_of_tweets, num_of_words):

    # start chrome driver:
    driver = init_driver()

    # log in to twitter:
    login_twitter(driver, username, password)

    # get the last n tweets as a string:
    tweets = last_n_tweets(driver, account_url, num_of_tweets)

    # if last_n_tweets returned an empty string:
    if tweets == "":
        # erase tweets.txt previous content:
        empty('tweets.txt')
        # erase output.txt previous content:
        empty('output.txt')

        with open('output.txt', 'a') as output:
            output.write('No tweets found for the account: ')
            output.write(account_url)
        driver.quit()
        exit(0)

    # make a list of hashtags:
    hashtags = re.findall(r'[#]\w+', tweets)

    # make a list of mentions:
    mentions = re.findall(r'[@]\w+', tweets)

    # count the most common words, stripping them of punctuation and numbers:
    word_counts = Counter(tweets.translate({ord(char): None for char in punctuation} and {ord(num): None for num in
                                                                                          "1234567890\".-…–"}).lower().split()).most_common(
        num_of_words)

    # if word_counts is empty, there are no actual words in any of the tweets:
    if not word_counts:
        # erase output.txt previous content:
        empty('output.txt')

        with open('output.txt', 'a') as output:
            output.write("No words were found in any of the tweets.")
        driver.quit()
        exit(0)

    # pop last item:
    last_word = word_counts.pop()

    # erase tweets.txt previous content:
    empty('tweets.txt')

    # write tweets to file (for testing):
    with io.open('tweets.txt', 'w', encoding='utf8') as tweets_file:
        tweets_file.write(tweets)

    # erase output.txt previous content:
    empty('output.txt')

    with io.open('output.txt', 'a', encoding='utf8') as output:
        if not hashtags:
            output.write('No hashtags were found in any of the tweets.')
        else:
            output.write('Hashtag list:\n')
            output.write(', '.join(h for h in hashtags))
        output.write('\n\n\n')
        if not mentions:
            output.write('No mentions were found in any of the tweets.')
        else:
            output.write('Mention list:\n')
            output.write(', '.join(m for m in mentions))
        output.write('\n\n\n')
        output.write('Word statistics:\n')
        for item in word_counts:
            output.write("{}: {} times,".format(*item))
            output.write(' ')
        output.write("{}: {} times.".format(*last_word))

    # close the browser window and quit the driver:
    driver.stop_client()
    driver.quit()


if __name__ == "__main__":
    # params:
    # 1. username
    # 2. password
    # 3. account url
    # 4. number of tweets to get
    # 5. number of words to count for statistics

    main("0547334542", "assignment", "https://twitter.com/realDonaldTrump", 100, 10)
