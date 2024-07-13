from operation import Stack

# every opening symbol has a corresponding closing symbol in the correct order
def is_balanced(expression):
    stack = Stack()
    matching_parentheses = {')':'(','}':'{',']':'['}
    
    for char in expression:
        if char in matching_parentheses.values:
            stack.push(char)
        elif char in matching_parentheses.keys:
            if stack.is_empty() or stack.pop() != matching_parentheses[char]:
                return False
    return stack.is_empty()

# Implement min_stack 
class Min_Stack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self,value):
        self.stack.append(value)
        if not self.min_stack or self.min_stack[-1] >= value:
            self.min_stack.append(value)
        
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        return self.stack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def get_min(self):
        return self.min_stack[-1]
    
# Reverse the stack using recursion
def insert(stack,temp):
    if stack.is_empty():
        stack.push(temp)
    else:
        item = stack.pop()
        insert(stack,temp)
        stack.push(item)
        
def reverse(stack):
    if not stack.is_empty():
        temp = stack.pop()
        reverse(stack)
        insert(stack,temp)
    
# reverse(stack)

# Next Greater element in stack
def second_greatest_element(stack):
    if stack.size() == 1 or stack.size() == 0:
        return False
    def finding(stack):
        if stack.is_empty():
           return float('-inf')
        temp = stack.pop()
        max_val = finding(stack)
        stack.push(temp)
        return max(max_val,temp)
    return finding(stack)
    
# second_greatest_element(stack)

# Next greater element of all of elements
def next_greater(arr):
    stack = []
    result = [-1]*len(arr)
    
    for i in range(len(arr)-1,-1,-1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])
        
    return result

arr = [4, 5, 2, 25]
next_greater(arr)
        

# sort a stack such that the smallest items are on the top
def insert_recursive(stack,val):
    if stack.is_empty() or stack.peek() > val:
        stack.push(val)
    else:
        temp = stack.pop()
        insert_recursive(stack,val)
        stack.push(temp)
        
def sort_recursive(stack):
    if not stack.is_empty():
        temp = stack.pop()
        sort_recursive(stack)
        insert_recursive(stack,temp)
    return stack

# Sorting using temporary stack
def sort_temp_stack(stack):
    temp_stack = Stack()
    while not stack.is_empty():
        temp = stack.pop()
        while not temp_stack.is_empty() and temp_stack.peek() > temp:
            stack.push(temp_stack.pop())
        temp_stack.push(temp)
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())
    return stack

stack = Stack()
stack.push(2)
stack.push(1)
stack.push(5)
stack.push(3)
print(sort_temp_stack(stack))