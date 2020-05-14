# Describe the scope of the variables a, b, c and d in this example: 
# def my_function(a):     
# b = a - 2 
#    return b 
#        c = 3 
 
#        if c > 2:     
# d = my_function(5) 
#   print(d) 
# What is the lifetime of these variables? When will they be created and destroyed? 
# Can you guess what would happen if we were to assign c a value of 1 instead? 
# Why would this be a problem? Can you think of a way to avoid it? 

def my_function(a):   
    b = a - 2 
    return b 
c = 3
if c > 2:     
    d = my_function(5) 
    print(d) 
