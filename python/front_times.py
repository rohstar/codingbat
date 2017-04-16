def front_times(str, n):

  res = ''
  shorterThanThree = len(str) < 3
  
  while(n != 0):
    
    if(shorterThanThree):
      res += str
    else:
      res += str[0:3]
    
    n = n - 1
    
  return res  