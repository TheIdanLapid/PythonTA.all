from huffman import *
from LZ77 import *
def genString(n):
    freq = 'a'*25+'bcdefghijklmnopqrstuvwxyz'
    randLetters = [random.choice(freq) for i in range(n)]
    return ''.join(randLetters)

s=genString(10000)
