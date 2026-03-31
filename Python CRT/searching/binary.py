def binarysearch(arr,target,pivot=0):
  if len(arr)==0:
    print( "Element does not exist")
  
  else:
    mid=len(arr)//2
    if target==arr[mid]:
      print (f"Element found at {mid+pivot} index")
    
    else:
      if(target<arr[mid]):
        return binarysearch(arr[:mid],target,pivot)
      elif target>arr[mid]:
        return binarysearch(arr[mid+1:],target,pivot+mid+1)
      else:
        print("Element doesnot exist")
output=binarysearch([1,2,3,4,5],5)