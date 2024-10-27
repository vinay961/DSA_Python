# Two sum problem
def two_sum(nums,target):
    num_map = {}
    
    for i,num in enumerate(nums):    # here enumerate help us to operate with index and value together. 
        complement = target-num
        if complement in num_map:
            return [num_map[complement],i]
        num_map[num] = i
    return []

        
# First Non-Repeating Character
def first_non_repeating_character(s):
    count = {}
    for ch in s:
        count[ch] = count.get(ch,0) + 1 # here get method first find the ch in count dict if it present there than it return the value corresponding to it, otherwise return the default value that is given as 0.
    
    for ch in s:
        if count[ch] == 1:
            return ch
    return None

