
class Node:
    def __init__(self,data):
        self.data = data
        self.next = Node
    
class LinkedListStack:
    def __init__(self):
        self.head = None
        self.count = 0
    
    def is_empty(self):
        return self.head is None
    
    def push(self,value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        self.count += 1
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Trying to pop from empty stack.")
        
        value = self.head.data
        self.head = self.head.next
        self.count -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.head.data
    
    def size(self):
        return self.count
    
    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return str(result)
def main():
    stack = LinkedListStack()

    while True:
        print("\n1. Push element")
        print("2. Pop element")
        print("3. Peek element")
        print("4. Check if stack is empty")
        print("5. Get stack size")
        print("6. Print stack")
        print("7. Exit")
        
        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            item = int(input("Enter the element to push: "))
            stack.push(item)
            print(f"{item} pushed to stack.")
        elif choice == 2:
            try:
                popped_item = stack.pop()
                print(f"Popped element: {popped_item}")
            except IndexError as e:
                print(e)
        elif choice == 3:
            try:
                top_item = stack.peek()
                print(f"Top element: {top_item}")
            except IndexError as e:
                print(e)
        elif choice == 4:
            if stack.is_empty():
                print("Stack is empty.")
            else:
                print("Stack is not empty.")
        elif choice == 5:
            print(f"Stack size: {stack.size()}")
        elif choice == 6:
            print(f"Stack: {stack}")
        elif choice == 7:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    
        