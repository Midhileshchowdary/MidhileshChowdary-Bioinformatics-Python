'''
find maximum element in list using recursion
'''
def find_max(arr, index=0):
    if index == len(arr) - 1:
        return arr[index]
    max_rest = find_max(arr, index + 1)
    return arr[index] if arr[index] > max_rest else max_rest
arr=[10,20,30,40]
print(find_max(arr))