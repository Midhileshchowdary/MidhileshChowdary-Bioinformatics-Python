'''
1.store 10 student names
2. swap the positions of any 2 students
3. print new seating arrangement
'''
list=[]
for i in range (10):
    temp=input(f"Enter the {i+1} Student Name : ")
    list.append(temp)
print(f"Original seating : {list}")
b=input("Enter the 1st student name to swap: ")
student_1=list.index(b)
c=input("Enter the 2nd student name to swap: ")
student_2=list.index(c)
t=list[student_1]
list[student_1]=list[student_2]
list[student_2]=t
print(f"Modified list : {list}")
