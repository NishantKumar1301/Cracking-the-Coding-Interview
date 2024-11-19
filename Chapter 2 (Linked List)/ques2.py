"""Question2 : Return Kth to Last: Implement an algorithm to find the kth to last element
of a singly linked list."""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        temp_node = self.head
        ans = ""
        while temp_node is not None:
            ans += str(temp_node.value)
            if temp_node.next is not None:
                ans += " -> "
            temp_node = temp_node.next
        return ans

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node


# Method 1: Using Length of the linked list  => Time complexity = O(2n)
def findKthToLastUsingLength(head, k):
    """
    :type head: Node
    :type k: int
    :rtype: Node
    Find the kth to last element in the list when the length is known.
    Implement your logic here.
    """
    # Complete your method
    length =0
    temp = head
    while temp is not None:
        length +=1
        temp = temp.next 
    position = length -k
    dummy = head
    
    for i in range(position-1):
        dummy = dummy.next 
    if position ==0 :
            popped_node = head
            head = head.next 
            return popped_node
    else:
        popped_node= dummy.next
        dummy.next = dummy.next.next 
        return popped_node
        
        


# Method 2: Iterative Approach => More optimal solution , Time complexity = O(n)
def findKthToLastIterative(head, k):
    """
    :type head: Node
    :type k: int
    :rtype: Node
    Find the kth to last element using an iterative approach.
    """
    slow = fast = head

    for i in range(k):
        if fast is None:
            return None  
        fast = fast.next

    while fast is not None:
        slow = slow.next
        fast = fast.next

    return slow



# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    values = [int(x) for x in input("Enter linked list values separated by space: ").split()]
    for value in values:
        ll.append(value)

    print("Original Linked List:")
    print(ll)

    k = int(input("Enter value for k: "))
    
    # Method 1: Using length
    result = findKthToLastUsingLength(ll.head, k)
    print(f"Kth to Last Element using length: {result.value}")
    
    print("New Linked List After removing the kth element from the method 1: ")
    print(ll)

    # Method 2: Iterative approach
    result = findKthToLastIterative(ll.head, k)
    print(f"Kth to Last Element using iterative: {result.value}")

