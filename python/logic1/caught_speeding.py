#You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.

def caught_speeding(speed, is_birthday):
  
  if(is_birthday):
    if(speed < 66):
      return 0
    if(speed > 65 and speed < 86):
      return 1  
    if(speed > 86):
      return 2 
  else: 
    if(speed < 61):
      return 0
    if(speed > 61 and speed < 81):
      return 1  
    if(speed > 81):
      return 2 
    
