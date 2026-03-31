#create list
Cartoons=['Tom & Jerry','Doremon','oggy&cockroach','shinchan']
duplicate_list= ['Tom & Jerry','Doremon','oggy&cockroach','shinchan']
print(Cartoons)
#add another element at end (APPEND)
print ("After Appending :")
Cartoons.append('pinkpanther')
print(Cartoons)
#insert element in required position (INSERT)
Cartoons.insert(0,'chotabheem')
print(Cartoons)
#remove last element (POP)
Cartoons.pop()
print(Cartoons)
#pop for removing particular index (POP(N))
Cartoons.pop(0)
print(Cartoons)
#remove element ( only removes the 1st occurance of the element in the list)
Cartoons.remove('shinchan')
print(Cartoons)
#print index of element
print(Cartoons.index('Doremon'))
#reversing the list
duplicate_list.reverse()
print(duplicate_list)
#sort
duplicate_list.sort()
print(duplicate_list)
#extend (add another list at end)
prog_lang=['C','C++','Python','Java']
print(prog_lang)
front_end=['HTML','CSS','Javascript','React JS']
print(front_end)
prog_lang.extend(front_end)
print(prog_lang)
database=['SQL','MySql']
prog_lang.extend(database)
print(prog_lang)
#count() is used to coutn the occurance of element in list
print(prog_lang.count('HTML'))