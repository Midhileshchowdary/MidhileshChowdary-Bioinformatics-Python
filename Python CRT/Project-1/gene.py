List=[]
result=[]
size=int(input("Enter the count of data : "))
for i in range(size):
    temp=float(input(f"Enter the expression value :"))
    List.append(temp)
print(f"User entered list : {List}")
for i in List:
    if i < 5:
        result.append("Underexpressed")
    elif i>=5 and i<=15:
        result.append("Normal")
    else:
        result.append("Overexpressed")
print(f"Exptrssion list : {result}")