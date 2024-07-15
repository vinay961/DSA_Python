import heapq

nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
heapq.heapify(nums)


heap = []
def insertion(key):
    return heapq.heappush(heap,key)

def deletion():
    return heapq.heappop(heap)

def peek():
    print(heap[0])
    
def main():
    while True:
        print("Choose one of them -->")
        print("1.Insertion..")
        print("2.Deletion..")
        print("3.Peek Element..")
        x = int(input("What operation??"))
        if x in [1,2,3]:
            break
    if x==1:
        key = int(input("What value??"))
        try:
            insertion(key)
            print("Element inserted successfully.")
        except:
            raise ValueError("Get error while insertion")
    if x==2:
        try:
            deletion(key)
            print("Element deleted successfully.")
        except:
            raise ValueError("Get error while deletion of element.")
    if x==3:
        peek()
    
if __name__ == "__main__":
    main()