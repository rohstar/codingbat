#Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

def last2(str):
  
  n = len(str)
  targetStr = str[n-2:]
  
  count = 0
  hits = 0
  
  while (count < n - 2):
    if(str[count:count+2] == targetStr):
      hits += 1
    count+= 1  
  
  return hits    
  
