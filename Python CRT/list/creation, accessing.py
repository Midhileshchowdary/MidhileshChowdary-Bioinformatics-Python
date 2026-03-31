#list creation and accessing
#     0, 1, 2, 3, 4, 5, 6, 7, 8
Num=[10,20,30,40,50,60,70,80,90]
#    -9,-8,-7,-6,-5,-4,-3,-2,-1
print(Num) # to print complete list
print("Accessing the list elememts using +ve index")
print(Num[0])
print(Num[1])
print(Num[2])
print(Num[3])
print(Num[4])
print(Num[5])
print(Num[6])
print(Num[7])
print(Num[8])
print("Accessing the list elememts using -ve index")
print(Num[-9])
print(Num[-8])
print(Num[-7])
print(Num[-6])
print(Num[-5])
print(Num[-4])
print(Num[-3])
print(Num[-2])
print(Num[-1])
#FOR LOOP->>>  +ve indexing
print("Accessing the list elememts using \"FOR loop without index\"")
for i in Num:
    print(i)
#range(start,stop,stepsize), range(start,stop), range(stop)
# below part give index positions
print("Index position of list")
for i in range(len(Num)):
    print(i)
print("Accessing the list elememts using \"FOR loop with index\"")
for i in range(len(Num)):
    print(Num[i])
#WHILE LOOP->>>   +ve indexing
print("Accessing the list elememts using \"WHILE loop with index\"")
i=0
while(i<len(Num)):
    print(Num[i])
    i+=1