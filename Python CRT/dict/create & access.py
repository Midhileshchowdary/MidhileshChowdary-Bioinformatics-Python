#example1
Dict={101:'Python',102:'Java',103:'SQL',104:'Javascript'}
print(Dict)
print(type(Dict))
print(Dict[101])

#example2
#creating
Stu={101:'Jyo',102:'Rev',103:'HAR'}
Fees={'Jyo':2000,'Rev':3000,'HAR':5000}
#accessing complete dict
print(Stu)
#accessing req element
print(Stu[101])
print(Stu[102])
print(Stu[103])
print(Fees['HAR'])
print(Fees['Jyo'])
print(Fees['Rev'])
#modification
Fees['Jyo']=2500
Stu[102]='Reavthi'
print(Stu)
print(Fees)