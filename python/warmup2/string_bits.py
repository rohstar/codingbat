#Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

def string_bits(str):
  
  n = len(str)

  count = 0
  res = ''
  
  while(count < n):
    #count is 2, res add str2
    
    res += str[count]
    count += 2
    
  return res
