class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def traverse(head):
    current = head
    while current:
        print(current.data , end=" -> ")
        current = current.next
    print("None")

def insert_at_beginning(head,data):
    new_Node = Node(data)
    new_Node.next = head
    head = new_Node
    return head

def insert_at_end(head,data):
    new_Node = Node(data)
    if not head:
        return new_Node
    
    current = head
    while current.next:
        current=current.next
    current.next = new_Node
    return head

def insert_at_specific_position(head,data,position):
    new_Node = Node(data)
    
    if position == 0:
        new_Node.next = head
        head = new_Node
        return head
    
    current = head
    for _ in range(position-1):
        current = current.next
    new_Node.next = current.next
    current.next = new_Node
    
    return head
        
def delete_from_beginning(head):
    if not head:
        return None
    
    return head.next

def delete_from_end(head):
    if not head or not head.next:
        return None
    current = head
    while current.next.next:
        current = current.next
    current.next = None
    return head

def delete_from_specific_position(head,position):
    if position == 0:
        return head.next
    
    current = head
    for _ in range(position-1):
        current = current.next
    current.next = current.next.next
    return head

def reverse_list(head):
    if not head:
        return print("List is empty")
    if head.next == None:
        return head
    
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def detect_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            print("LinkedList contain cycle.")
    return False

def find_middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data

def main():
    head = None
    while True:
        print("\nChoose an operation:")
        print("1. Traverse")
        print("2. Insert at beginning")
        print("3. Insert at end")
        print("4. Insert at specific position")
        print("5. Delete from beginning")
        print("6. Delete from end")
        print("7. Delete from specific position")
        print("8. Reverse the list")
        print("9. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            traverse(head)
        elif choice == 2:
            data = int(input("Enter data to insert at beginning: "))
            head = insert_at_beginning(head, data)
        elif choice == 3:
            data = int(input("Enter data to insert at end: "))
            head = insert_at_end(head, data)
        elif choice == 4:
            data = int(input("Enter data to insert: "))
            position = int(input("Enter position to insert at: "))
            head = insert_at_specific_position(head, data, position)
        elif choice == 5:
            head = delete_from_beginning(head)
        elif choice == 6:
            head = delete_from_end(head)
        elif choice == 7:
            position = int(input("Enter position to delete from: "))
            head = delete_from_specific_position(head, position)
        elif choice == 8:
            head = reverse_list(head)
        elif choice == 9:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

    