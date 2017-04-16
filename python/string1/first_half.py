#Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".


def first_half(str):
  nby2 = len(str) / 2
  
  return str[:nby2]
