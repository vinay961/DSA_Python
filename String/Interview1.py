# Find the first non-repeating character

def first_non_repeated_char(s):
    dict = {}
    
    for char in s:
        dict[char] = dict.get(char,0)+1 # here dict.get(char,0) -> search for current char if it founds then it return there current count, else return the default value which is 0.
    for char in s:
        if dict[char] == 1:
            return char
    return None

# Count number of vowels in the string

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Longest common prefix

def longest_common_prefix(strs):
    if not strs:
        return " "
    prefix = strs[0]
    for string in strs[1:]:
        while string[:len(prefix)] != prefix:
            prefix = prefix[:-1]
            if not prefix:
                return " "
    return prefix

# Find all permutations of string

from itertools import permutations

def find_permutations(s):
    return [''.join(p) for p in permutations(s)]

# Check if one string is a rotation of another using a substring method.

def rotation(s1,s2):
    if len(s1) != len(s2):
        return False
    
    return s2 in s1+s1

# Check strings are anagram or not

def check_anagram(s1,s2):
    if len(s1) != len(s2):
        return False
    for char in s1:
        if char not in s2:
            return False
    return True

# Check that two strings are k-anagram or not

def k_anagram(s1,s2,k):
    if len(s1) != len(s2):
        return False
    
    dict1 = {}
    dict2 = {}
    
    for char in s1:
        dict1[char] = dict1.get(char,0) + 1
    for char in s2:
        dict2[char] = dict2.get(char,0) + 1
    
    changes_needed = 0
    for char in s1:
        if char in s2:
            if dict1[char] > dict2[char]:
                changes_needed += dict1[char] - dict2[char]
            else:
                changes_needed += dict1[char]
        
    print(changes_needed)
    return changes_needed <= k
                

print(k_anagram("evil","ilev",2))
    
