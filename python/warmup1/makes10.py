def makes10(a, b):

  oneIsTen = False

  if(a == 10 or b == 10):
    oneIsTen = True
  
  if(oneIsTen or (a+b == 10)):
    return True
    
  return False  
