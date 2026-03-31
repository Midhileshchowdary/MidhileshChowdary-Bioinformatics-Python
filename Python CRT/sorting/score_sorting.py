'''
Your task is to sort the array in ascending order using a basic
sorting algorithm (Bubble Sort / Selection Sort / Insertion Sort).
Input:
An integer n (1<= n <= 1000) - number of students
An array of n integers - the scores (0<= score <= 100)Output:
Sorted array of scores in ascending order Example;
Input:5
Scores:[55, 90, 70,60, 80]
output:[55, 60, 70, 80，90]
'''
Scores=[55,90,70,60,80]
Length=len(Scores)
print("Original array :",Scores)
for i in range(Length-1):
    for j in range(Length-i-1):
        if Scores[j]>Scores[j+1]:
            temp=Scores[j]
            Scores[j]=Scores[j+1]
            Scores[j+1]=temp
print("Output: ",Scores)

def insertionsort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key <arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
print("Output : ", insertionsort([55, 90, 70,60, 80]))