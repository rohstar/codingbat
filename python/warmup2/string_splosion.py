
#Given a non-empty string like "Code" return a string like "CCoCodCode".

def string_splosion(str):
  
  n = len(str)
  count = 0;
  res = ''
  
  while( count < n ):
    
    res += str[:count+1]
    count += 1
    
  return res  
  
  
