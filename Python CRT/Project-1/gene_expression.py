size = int(input("enter the size of list: "))
list= []
list2 = []
for i in range(size):
    temp = float(input("enter the gene expression data: "))
    list.append(temp)
print(list)
for i in range(size):
    if list[i] < 5:
        list2.append("Underexpressed")
    elif list[i] >= 5 and list[i] <= 15:
        list2.append("Normal")
    elif list[i] > 15 :
        list2.append("Overexpressed")
print(list)
print(list2)