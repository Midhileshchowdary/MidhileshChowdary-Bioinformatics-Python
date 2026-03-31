'''
1.Add 10 songs to the playlist
2.show playlist in normal and reverse order
'''
List=[]
for i in range(10):
    temp=input(f"Enter the {i+1} song name :")
    List.append(temp)
print(f"List in normal order : {List}")
print("List in reverse order :",List[::-1])