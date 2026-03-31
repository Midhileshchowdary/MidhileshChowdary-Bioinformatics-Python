'''def function_name (parameters):
	if base_condition:
		return result
	return function_name(modified_parameters)'''
List=[10,20,30,40,50,60,70,80,90,100]
def Add_list(List):
    if len(List)==0:
        return 0
    return List[0]+Add_list(List[1:])
print(Add_list(List))

def Add_List(n,Sum):
    if bool(n):
        Sum+=n
        return Add_List(n-1,Sum)
    return Sum
print(Add_List(5,0))
# write py prog to print the summation of list elements
Li=[1,2,3,4,5]
def Add_List(List,Sum):
    if bool(List[len(List)-1]):
        Sum=Sum+List[len(List)-1]
        return Add_List(List.pop(),Sum)
    return Sum
print(Add_List(Li,0))
