class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)

def main():
    stack = Stack()
    
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
