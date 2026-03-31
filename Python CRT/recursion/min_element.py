'''
find minimum element in list using recursion
'''

def find_min(arr, index=0):
    if index == len(arr) - 1:
        return arr[index]
    min_rest = find_min(arr, index + 1)
    return arr[index] if arr[index] < min_rest else min_rest

# Example list
arr = [25, 10, 45, 5, 30]
print("Minimum element is:", find_min(arr))
