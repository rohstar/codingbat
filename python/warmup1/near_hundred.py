def near_hundred(n):
  
  diff100 = abs(n-100)
  diff200 = abs(n-200)
  
  if(diff100 < 11 or diff200 < 11):
    return True
    
  return False  
