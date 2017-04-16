def parrot_trouble(talking, hour):
  
  inRange = hour < 7 or hour > 20
  
  if( inRange and talking ):
    return True
    
  return False  
