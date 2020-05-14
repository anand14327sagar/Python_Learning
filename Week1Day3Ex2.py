#Given a list iterate it and display numbers which are divisible by 3 and if you find number greater than 150 stop the loop iteration 

list = [12, 14, 33, 43, 55, 75, 99, 132, 150, 180, 200]
list1 = []
for i in list: 
    # print(i)
    if(i % 3 == 0):
        if(i < 150):
            list1.append(i)
        else:
            break    
print("The final list of numbers are:"+ str(list1))