Arr=[10,20,48,5,2,34,24,79,52]
Length=len(Arr)
print("Original array :",Arr)
for i in range(Length-1):
    for j in range(Length-i-1):
        if Arr[j]>Arr[j+1]:
            temp=Arr[j]
            Arr[j]=Arr[j+1]
            Arr[j+1]=temp
print("Sorted Array : ",Arr)

#using functions
Arr=[25,20,15,10,5]
for i in range(len(Arr)):
    Flag=False
    for j in range(len(Arr)-1):
        if(Arr[j]>Arr[j+1]):
            Arr[j],Arr[j+1]=Arr[j+1],Arr[j]
            print(Arr)
            Flag=True
    if Flag==False:
        break
print(Arr)
