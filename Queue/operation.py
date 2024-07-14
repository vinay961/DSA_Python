# Queue implementation 
class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self,item):
        self.items.append(item)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            raise IndexError("Queue is empty, so there is no any front element.")
        return self.items[0]
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
                      
# Queue implementation using linkedlist
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedlistQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0
    
    def is_empty(self):
        return self.fornt is None
    
    def enqueue(self,val):
        new_node = Node(val)
        if self.rear:
            self.rear.next = new_node
        self.rear = new_node
        if not self.front:
            self.front = new_node
        count += 1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Trying to dequeue from empty queue.")
        temp = self.front.data
        self.front = self.front.next
        if not self.front:
            self.rear = None
        self.count -= 1
        return temp
    
    def front(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.front.data
    
    def size(self):
        return self.count
    
    def __str__(self):
        result = []
        current = self.front
        while current:
            result.append(current.data)
            current = current.next
        return str(result)

# Implement queue using stack
class Queue_Using_Stack:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
        count = 0
        
    def enqueue(self,val):
        self.in_stack.append(val)
        count += 1
    
    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.out_stack.pop())
                
        if not self.out_stack:
            raise IndexError("dequeue from empty queue.")
        count -= 1
        return self.out_stack.pop()
        
    def size(self):
        return self.count
    
    def __str__(self):
        return str(self.in_stack)

def main():
    print("Choose the type of queue you want to work with:")
    print("1. List-based Queue")
    print("2. Linked List-based Queue")
    print("3. Queue using Stacks")
    
    choice = int(input("Enter your choice (1/2/3): "))
    
    if choice == 1:
        queue = Queue()
    elif choice == 2:
        queue = LinkedlistQueue()
    elif choice == 3:
        queue = Queue_Using_Stack()
    else:
        print("Invalid choice.")
        return
    
    while True:
        print("\nChoose an operation:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Front")
        print("4. Size")
        print("5. Display")
        print("6. Exit")
        
        operation = int(input("Enter your choice: "))
        
        if operation == 1:
            value = input("Enter the value to enqueue: ")
            queue.enqueue(value)
        elif operation == 2:
            try:
                dequeued_value = queue.dequeue()
                print(f"Dequeued value: {dequeued_value}")
            except IndexError as e:
                print(e)
        elif operation == 3:
            try:
                front_value = queue.front()
                print(f"Front value: {front_value}")
            except IndexError as e:
                print(e)
        elif operation == 4:
            print(f"Queue size: {queue.size()}")
        elif operation == 5:
            print(f"Queue: {queue}")
        elif operation == 6:
            break
        else:
            print("Invalid operation.")

if __name__ == "__main__":
    main()

      
        
    
        
    