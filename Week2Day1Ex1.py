
def convert(list): 
    return tuple(list) 
  
# Driver function 
sampleList = [1, 4, 1, 5, 4, 4, 9, 9] 
sampleList = list(dict.fromkeys(sampleList))
sampleTuple = convert(sampleList)
print("This is the List:",sampleList)
print("This is the Tuple:",sampleTuple)
print("The min value is:",min(sampleTuple))
print("The max value is:",max(sampleTuple))