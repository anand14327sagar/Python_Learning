# Python program for implementation of Bubble Sort 
  
def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n-1): 
  
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
  
sampleData = [25, 6, 89, 7, 10, 1, 99, 70, 55] 
bubbleSort(sampleData) 
  
print ("Sorted array is:") 
for i in range(len(sampleData)): 
    print ("%d" %sampleData[i]),