def front_back(str):

  n = len(str)

  if(n < 2):
    return str

  return str[n - 1] + str[1:n - 1] + str[0]  
