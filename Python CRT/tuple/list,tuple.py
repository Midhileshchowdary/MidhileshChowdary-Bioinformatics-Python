# write a python program to declare a list of words and ddeclared a tuple of words and map it to print the combined words
n=int(input("enter the number of words r=that you would like to find : "))
List=['marker','black','jim','class']
Tuple=('pen','board','jam','room')
i=1
while(i<=n):
    word=input("enter the word: ")
    index=List.index(word)
    print(f"{word}-{Tuple[index]}")
    i+=1