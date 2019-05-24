import math

def str_to_ascii(text):
  """ Gets rid of on ascii characters in text"""
  return ''.join(ch for ch in text if ord(ch)<128)


def maxmatch(T, p, w=2**12-1, max_length=2**5-1):
   """ finds a maximum match of length k<=2**5-1 in a
   w long window, T[p:p+k] with T[p-m:p-m+k].
   Returns m (offset) and k (match length) """
   assert isinstance(T,str)
   n = len(T)
   maxmatch = 0
   offset = 0
   for m in range(1, min(p+1, w)):
      k = 0
      while k < min(n-p, max_length) and T[p-m+k] == T[p+k]:
        k += 1
        # at this point, T[p-m:p-m+k]==T[p:p+k]
      if maxmatch < k:  
         maxmatch = k
         offset = m
   return offset, maxmatch
# returned offset is smallest one (closest to p) among
# all max matches (m starts at 1)



def lz77_compress(text, w=2**12-1, max_length=2**5-1):
   """LZ77 compression of an ascii text. Produces
      a list comprising of either ascii characters
      or pairs [m,k] where m is an offset and
      k is a match (both are non negative integers)"""
   result = []
   n = len(text)
   p = 0
   while p<n:
      if ord(text[p]) >= 128: continue
      m,k = maxmatch(text, p, w, max_length)
      if k<2:
         result.append(text[p]) #  a single char
         p += 1
      else:
         result.append([m,k])   # two or more chars in match
         p += k
   return result  # produces a list composed of chars and pairs
            
                          
def lz77_decompress(compressed, w=2**12-1, max_length=2**5-1):
   """LZ77 decompression from intermediate format to ascii text"""
   result = []
   n = len(compressed)
   p = 0
   while p<n:
      if type(compressed[p]) == str:  # char, as opposed to a pair
         result.append(compressed[p])
         p+=1
      else:
         m,k = compressed[p]
         p += 1
         for i in range(0,k):
            # append k times to result;  
            result.append(result[-m])
            # fixed offset m "to the left", as result itself grows
   return lst_to_string(result)


def lst_to_string(lst):
  """ converting a list of chars to a string """
  return "".join (ch for ch in lst)

      
def lz77_compress2(text, w=2**12-1, max_length=2**5-1):
   """LZ77 compression of an ascii text. Produces
      a list comprising of either ascii character
      or by a pair [m,k] where m is an offset and
      k>3 is a match (both are non negative integers)"""
   result = []
   out_string = ""
   n = len(text)
   p = 0
   while p<n:
      if ord(text[p]) >= 128: continue
      m,k = maxmatch(text, p, w, max_length)
      if k<4:   # modified from k<2
         result.append(text[p]) # a single char
         p += 1 #even if k was 2 (why?)
      else:
         result.append([m,k])   # two or more chars in match
         p += k
   return result  # produces a list composed of chars and pairs
            
            

def inter_to_bin(lst, w=2**12-1, max_length=2**5-1):
   """ converts intermediate format compressed list
       to a string of bits"""
   offset_width = math.ceil(math.log(w,2))
   match_width = math.ceil(math.log(max_length, 2))
   #print(offset_width,match_width)   # for debugging
   result = []
   for elem in lst:
      if type(elem) == str:
         result.append("0")
         result.append('{:07b}'.format(ord(elem)))
      elif type(elem) == list:
         result.append("1")
         m,k = elem
         result.append('{num:0{width}b}'.format
                       (num=m, width=offset_width))
         result.append('{num:0{width}b}'.
                       format(num=k, width=match_width))
         
   return "".join(ch for ch in result)
   
   
                         
def bin_to_inter(compressed, w=2**12-1, max_length=2**5-1):
   """ converts a compressed string of bits
       to intermediate compressed format """
   offset_width = math.ceil(math.log(w,2))
   match_width = math.ceil(math.log(max_length,2))
   #print(offset_width,match_width)   # for debugging
   result = []
   n = len(compressed)
   p = 0
   while p<n:
      if compressed[p] == "0":  # single ascii char
         p += 1
         char = chr(int(compressed[p:p+7], 2))
         result.append(char)
         p += 7
      elif compressed[p] == "1":  # repeat of length > 2
         p += 1
         m = int(compressed[p:p+offset_width],2)
         p += offset_width
         k = int(compressed[p:p+match_width],2)
         p += match_width
         result.append([m,k])
   return result
   

import urllib.request   
def process_nytimes():
  btext = urllib.request.urlopen('http://www.nytimes.com/').read()
  nytext = str_to_ascii ( btext.decode ('utf -8'))
  ny_inter = lz77_compress2(nytext)
  ny_bin = inter_to_bin(ny_inter)
  ny_inter2 = bin_to_inter(ny_bin)
  nytext2 = lz77_decompress(ny_inter2)
  print("NYT done")
  return nytext, ny_inter, ny_bin, ny_inter2, nytext2

def process(text):
         
  atext = str_to_ascii(text)
  inter = lz77_compress2(atext)
  bint = inter_to_bin(inter)
  inter2 = bin_to_inter(bint)
  text2 = lz77_decompress(inter)
  return inter, bint, inter2, text2

s ="aaabbbaaabbbaaa"
lst = [maxmatch(s,i) for i in range(len(s))]


text="""how much wood would the wood chuck chuck if the wood chuck
would chuck wood should could hood"""

lst2 = [maxmatch(text,i) for i in range(len(text))]

