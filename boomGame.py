#Question 3
in_file = "our_input.txt"
out_file = "output.txt"
tom = open(in_file, 'r')
out = open(out_file, 'w')
for line in tom:
    out.write(str(len(line.split()))+'\n')
out.close()


#**************************************************************
#Question 5
k = 3
n = 100
boom = k
end = n
count = 1
while (count < n+1):
    if (str(boom) in str(count) and count % boom == 0):
        print ("boom-boom!")
    elif (count % boom == 0 or str(boom) in str(count)):
        print("boom!")
    else:
        print(count)
    count += 1

        
#**************************************************************
#Question 6
input_str = input("Please enter a positive integer: ")
#Add the rest of your code here.
#It should handle any positive integer or an arithmetic expression
#at the end, length, start and seq should hold the answers

num = str(eval(input_str))
count = 0
odds =  ""
index = -1
seqtemp = ""
ind = 0

length = 0
start = -1
seq = None



for i in num:
    if int(i) % 2 != 0:
        count += 1
        odds += i
    else:
        if len(odds) > len(seqtemp):
            seqtemp = odds
            index = ind - count
        count = 0
        odds = ""
    ind += 1

if len(odds) > len(seqtemp):
    seqtemp = odds
    index = ind - len(odds)

if len(seqtemp) > 0 :
    length = len(seqtemp)
    start = index   
    seq = seqtemp


print("The maximal length is", length)
print("Sequence starts at", start)
print("Sequence is", seq)

