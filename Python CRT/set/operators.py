Set1={1,2,3,6}
Set2={3,4,5,6,7}
print(Set1|Set2) # unique items from both sets (union)
print(Set1 & Set2) # common elements in both sets
print(Set1-Set2) #element only in 1st set
print(Set1^Set2) # items in either sets but not both
print(Set1.union(Set2))
print(Set1.intersection(Set2))
print(Set1.difference(Set2))
Set3={3,4,5}
print(Set3.issubset(Set2)) #TRUE Set3 in set2
print(Set2.issuperset(Set3)) #TRUE set3 in set2
