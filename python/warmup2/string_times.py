#Given a string and a non-negative int n, return a larger string that is n copies of the original string.

def string_times(str, n):
  res = ''
  
  while(n != 0):
    res += str
    n = n - 1
    
  return res  
