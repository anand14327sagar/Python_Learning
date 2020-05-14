# Python program to find the sum of numbers from 0 to 20
def recur_sum(n):
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)

# change this value for a different result
num = 20

if num < 0:
   print("Enter a positive number")
else:
   sum = recur_sum(num)
   finalSum = sum - 1
   print("The sum of numbers from 2 to 20 is: "+str(finalSum))