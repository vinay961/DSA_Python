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
        count[ch] = count.get(ch,0) + 1 # here get method first find the ch in count dict if it present there than it return the value corresponding to it, otherwise return the default value that is set as 0.
    
    for ch in s:
        if count[ch] == 1:
            return ch
    return None


# Group Anagram
def group_anagrams(str):
    anagram_map = {}
    for s in str:
        key = ''.join(sorted(s))
        if key not in anagram_map:
            anagram_map[key]  = []
        anagram_map[key].append(s)
    return list(anagram_map.values())

# print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

# Subarray Sum Equals k
def subarray_sum(nums,k):
    sum_map = {0:1}
    count = 0
    current_sum = 0
    
    for num in nums:
        current_sum += num
        count += sum_map.get(current_sum-k,0)
        sum_map[current_sum] = sum_map.get(current_sum,0)+1;
    return count

from heapq import heappush, heappop
# Top k frequent element
def top_frequent(nums,k):
    freq_map = {}
    
    for num in nums:
        freq_map[num] = freq_map.get(num,0)+1
    heap = []
    for num,freq in freq_map.items():
        heappush(heap, (-freq,num))
    result = []
    for _ in range(k):
        most_freq = heappop(heap)
        result.append(most_freq[1])
    return result

print(top_frequent([1, 1, 1, 2, 2, 3], 2))
    