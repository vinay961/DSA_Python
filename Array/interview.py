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

# Moves zeroes to end
def handle_zeroes(arr):
    if not arr:
        return 0
    n = len(arr)
    index = 0
    for i in range(n):
        if arr[i] != 0:
            arr[index], arr[i] = arr[i], arr[index]
            index += 1
    return arr

# First and last position of element in array
def position_array(arr,k):
    first_index = 0
    second_index = 0
    flag1 = True
    flag2 = False
    for i in range(len(arr)):
        if arr[i] == k and flag1 == True:
            first_index = i
            flag1 = False
            flag2 = True
        if arr[i] == k and flag2 == True:
            second_index = i
    return [first_index+1,second_index+1]

# Product of array except itself
def product(arr):
    if not arr:
        return []
    n = len(arr)
    for i in range(n):
        y = 1
        x = arr[i]
        for j in range(n):
            if arr[j] != x:
                y *= arr[j]
        arr[i] = y
    return arr


# Rainwater trapping problem
def trap_rain_water(height):
    if not height:
        return 0
    left,right = 0,len(height)-1
    left_max,right_max = height[left],height[right]
    water_trapped = 0
    
    while left<right:
        if left_max<right_max:
            left += 1
            left_max = max(left_max,height[left])
            water_trapped += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max,height[right])
            water_trapped += right_max - height[right]
        
    return water_trapped


# Container which can store maaximum water
def container_with_maximum_water(height):
    left,right = 0,len(height)-1
    max_area = 0
    
    while left<right:
        area = min(height[left],height[right])*(right-left)
        max_area = max(area,max_area)
        
        if height[left]<height[right]:
            left += 1
        else:
            right -= 1
        
    return max_area

# Longest consecutive element sequence
def longest_consecutive_sequence(arr):
    if not arr:
        return []
    n = len(arr)
    count = 0
    for i in range(n):
        x = arr[i]
        temp = 0
        while True:
            x += 1
            if x in arr:
                temp += 1
            else:
                break
        count = max(count,temp+1)
    return count

# Find all unique triplets that gives sum zero
def triplets(arr):
    if not arr:
        return []
    arr.sort()
    result = []
    
    for i in range(len(arr)-2):
        if i>0 and arr[i] == arr[i-1]:
            continue
        left,right = i+1,len(arr)-1
        while left<right:
            total = arr[i]+arr[left]+arr[right]
            
            if total>0:
                right -= 1
            elif total<0:
                left += 1
            else:
                result.append([arr[i],arr[left],arr[right]])
                if left<right and arr[left] == arr[left+1]:
                    left += 1
                if left<right and arr[right] == arr[right-1]:
                    right -= 1
                left += 1
                right -= 1

    return result
    
        
