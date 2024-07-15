class CircularQueue:
    def __init__(self, k):
        self.queue = [None] * k
        self.max_size = k
        self.front = self.rear = -1
    
    def is_full(self):
        return ((self.rear + 1) % self.max_size) == self.front
    
    def is_empty(self):
        return self.front == -1
    
    def enqueue(self, val):
        if self.is_full():
            return False
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = val
        return True
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size
        return item
    
    def front_element(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.queue[self.front]
    
    def display(self):
        if self.is_empty():
            return []
        if self.rear >= self.front:
            return self.queue[self.front:self.rear+1]
        else:
            return self.queue[self.front:self.max_size] + self.queue[0:self.rear+1]

from collections import deque

def generate_binary_numbers(n):
    queue = deque()
    result = []
    queue.append("1")
    
    for _ in range(n):
        front = queue.popleft()
        result.append(front)
        queue.append(front + "0")
        queue.append(front + "1")
    
    return result

def is_palindrome(s):
    stack = []
    queue = deque()
    
    for char in s:
        stack.append(char)
        queue.append(char)
        
    while stack:
        if stack.pop() != queue.popleft():
            return False
    return True

import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []
        
    def is_empty(self):
        return len(self.heap) == 0
    
    def enqueue(self, item, priority):
        heapq.heappush(self.heap, (priority, item))
        
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Priority Queue is empty.")
        return heapq.heappop(self.heap)[1]
    
    def peek(self):
        if self.is_empty():
            return None
        return self.heap[0][1]

def main():
    while True:
        print("\nChoose an operation:")
        print("1. Circular Queue")
        print("2. Generate Binary Numbers")
        print("3. Check Palindrome")
        print("4. Priority Queue")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            print("\nCircular Queue Operations:")
            k = int(input("Enter the size of the queue: "))
            cq = CircularQueue(k)
            while True:
                print("\n1. Enqueue")
                print("2. Dequeue")
                print("3. Display")
                print("4. Back to Main Menu")
                op = int(input("Choose an operation: "))
                
                if op == 1:
                    val = int(input("Enter value to enqueue: "))
                    if cq.enqueue(val):
                        print("Enqueued successfully.")
                    else:
                        print("Queue is full.")
                elif op == 2:
                    try:
                        print("Dequeued value:", cq.dequeue())
                    except IndexError as e:
                        print(e)
                elif op == 3:
                    print("Queue elements:", cq.display())
                elif op == 4:
                    break
                else:
                    print("Invalid choice.")
        
        elif choice == 2:
            n = int(input("Enter the number of binary numbers to generate: "))
            print("Binary numbers:", generate_binary_numbers(n))
        
        elif choice == 3:
            s = input("Enter the string to check palindrome: ")
            if is_palindrome(s):
                print("The string is a palindrome.")
            else:
                print("The string is not a palindrome.")
        
        elif choice == 4:
            print("\nPriority Queue Operations:")
            pq = PriorityQueue()
            while True:
                print("\n1. Enqueue")
                print("2. Dequeue")
                print("3. Peek")
                print("4. Back to Main Menu")
                op = int(input("Choose an operation: "))
                
                if op == 1:
                    item = input("Enter item to enqueue: ")
                    priority = int(input("Enter priority: "))
                    pq.enqueue(item, priority)
                    print("Enqueued successfully.")
                elif op == 2:
                    try:
                        print("Dequeued item:", pq.dequeue())
                    except IndexError as e:
                        print(e)
                elif op == 3:
                    print("Peek item:", pq.peek())
                elif op == 4:
                    break
                else:
                    print("Invalid choice.")
        
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
