Job={101:'Full Stack Developer',102:'Data Engineer',103:'Data analyst',104:'tester'}
print(Job)
#adding elements
Job[105]='front end developer'
Job[106]='back end developer'
Job[107]='siftware developer'
print(Job)
#remove key element - pop 
Job.pop(101)
print(Job)
del Job[102]
print(Job)
#length of dict
print(len(Job))
#list of keys
print(Job.keys())
#list of values
print(Job.values())
# key value pairs as tuples---> items()
print(Job.items())
#copy method
Role=Job.copy()
print(Job)
#update method
B={1:'AB',2:'CD'}
Job.update(B)
print(Job)