# Subarray with maximum sum
def max_sum(arr):
    n = len(arr)
    try:
        sum = result = arr[0]
        for x in range(1,n):
            sum = max(arr[x],sum+arr[x])
            print(sum,end=' ')
            result = max(sum,result)
            print(result)
        
        print(result)
    except:
        if not n:
            raise IndexError("Array is empty.")

# smallest missing positive number
def missing_num(arr):
    n = len(arr)
    if not n :
        print("List is empty")
    x = float('inf')
    y = float('-inf')
    for i in range(n):
        if arr[i] > 0 and arr[i] < x:
            x = arr[i]
        if arr[i] > y:
            y = arr[i]
    for i in range(x,y+1):
        if i not in arr:
            print(i)

        
# Two sum problem
def two_sum(arr,target):
    n = len(arr)
    arr.sort()
    x = 0
    y = n-1
    
    while x != y:
        if arr[x]+arr[y] == target:
            return [x,y]
        elif arr[x]+arr[y] > target:
            y -+ 1
        else:
            x += 1

# Remove duplicates from sorted array
def remove_duplicate(arr):
    if not arr:
        return 0
    
    n = len(arr)
    index = 0
    
    for i in range(1,n):
        if arr[i] != arr[index]:
            index += 1
            arr[index] = arr[i]
            
    return arr[:index+1]

# Find duplicates in array
def duplicate(arr):
    if not arr:
        print("Array doesn't exist.")
    
    n = len(arr)
    result = []
    arr.sort()
    
    for i in range(1,n):
        if arr[i] == arr[i-1]:
            if arr[i] not in result:
                result.append(arr[i])
        
    return result

# Merge two sorted array
def merge_array(arr1,arr2):
    if not arr1 and arr2:
        return []
    n1 = len(arr1)
    n2 = len(arr2)
    result = []
    
    i = j = 0
    while i < n1 and j < n2:
        if arr1[i] > arr2[j]:
            result.append(arr2[j])
            j += 1
        elif arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr1[i])
            result.append(arr2[j])
            i += 1
            j += 1
    
    if i < n1:
        for x in range(i,n1):
            result.append(arr1[x])
    if j < n2:
        for x in range(j,n2):
            result.append(arr2[x])
    return result

# Rotate the array in right by k steps
def rotate_right(arr,k):
    if not arr:
        return 0
    
    n = len(arr)
    def reverse(sub_array,start,end):
        sub_array[start],sub_array[end] = sub_array[end],sub_array[start]
        start += 1
        end -= 1
        
    reverse(arr,0,n-1)
    reverse(arr,0,k-1)
    reverse(arr,k,n-1)

    return arr

print(rotate_right([1,2,3,4,5],3))
    