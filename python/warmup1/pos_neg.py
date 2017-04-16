def pos_neg(a, b, negative):
  
  aIsNeg = a < 0
  bIsNeg = b < 0
  
  if(negative):
    return aIsNeg and bIsNeg
    
  return aIsNeg != bIsNeg  
