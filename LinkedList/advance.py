# Merging two sorted Linked List
from operation import insert_at_end,traverse

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def merge_sorted_list(l1,l2):
    dummy = Node(0)
    current = dummy
    
    while l1 and l2:
        if l1.data < l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
        
        current.next = l1 if l1 else l2
        
    return dummy.next

def remove_from_end(head,position):
    current = head
    curr = head
    count=0
    while current:
        count+=1
        current = current.next
        
    count = count-position
    for _ in range(count-1):
        curr = curr.next
    curr.next = curr.next.next
    return head
    
def is_Palindrome(head):
    slow = fast = head
    stack = []
    
    while fast and fast.next:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next
    if fast:
        slow = slow.next
    while slow:
        if stack.pop() != slow.data:
            return False
        slow = slow.next    
    return True

def main():
    head1 = None
    head2 = None
    
    while True:
        print("\nChoose an operation:")
        print("1. Traverse List 1")
        print("2. Traverse List 2")
        print("3. Insert at end of List 1")
        print("4. Insert at end of List 2")
        print("5. Merge List 1 and List 2")
        print("6. Delete from end of List 1")
        print("7. Delete from end of List 2")
        print("8. Check palindrome")
        print("9. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            print("List 1: ", end="")
            traverse(head1)
            print("------------------------------------------------")
            
        elif choice == 2:
            print("List 2: ", end="")
            traverse(head2)
            print("------------------------------------------------")
            
        elif choice == 3:
            data = int(input("Enter data to insert at end of List 1: "))
            head1 = insert_at_end(head1, data)
            
        elif choice == 4:
            data = int(input("Enter data to insert at end of List 2: "))
            head2 = insert_at_end(head2, data)
            
        elif choice == 5:
            merged_head = merge_sorted_list(head1, head2)
            print("Merged List: ", end="")
            traverse(merged_head)
            print("------------------------------------------------")
            
        elif choice == 6:
            position = int(input("Position? "))
            head = remove_from_end(head1,position)
            print("New List: ", end="")
            traverse(head)
            print("------------------------------------------------")
            
        elif choice == 7:
            position = int(input("Position? "))
            head = remove_from_end(head2,position)
            print("New List: ", end="")
            traverse(head)
            print("------------------------------------------------")
            
        elif choice == 8:
            res = input("For which linked list(l1/l2)? ")
            if res == "l1":
                print(is_Palindrome(head1))
            else:
                print(is_Palindrome(head2))
                
        elif choice == 9:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
        