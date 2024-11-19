"""Question4: Palindrome: Implement a function to check if a linked list is a palindrome."""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def __str__(self):
        temp_node = self.head
        ans = ""
        while temp_node is not None:
            ans += str(temp_node.value)
            if temp_node.next is not None:
                ans += " -> "
            temp_node = temp_node.next
        return ans

# Helper Function to find the middle of the linked list

def findMiddleNode(head):
    slow = fast = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next 
        slow = slow.next
    return slow

# Helper Method for reversing a linked list from a given node

def reverseList(head):
    current = head
    previous = None
    while(current is not None):
        next_node = current.next 
        current.next = previous
        previous = current
        current=next_node
    return previous

# Method: Check if the linked list is a palindrome
def isPalindrome(head):
    """
    :type head: Node
    :rtype: bool
    Implement your logic here to check if the linked list is a palindrome.
    """
    if head is None or head.next is None:
        return True
    
    #Step1 : Find the middle of the linked list
    
    middle_element = findMiddleNode(head)
    
    #Step2 : Reverse the right half of the linked list
    
    right_half = reverseList(middle_element)
    
    #Step3 : Compare the left half and the reversed right half
    
    left_half = head
    
    while right_half is not None:
        if left_half.value != right_half.value:
            return False
        
        left_half = left_half.next 
        right_half = right_half.next

    return True


# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    values = [int(x) for x in input("Enter linked list values separated by space: ").split()]
    for value in values:
        ll.append(value)

    print("Linked List:")
    print(ll)

    # Method: Check if palindrome
    result = isPalindrome(ll.head)
    print(f"Is Palindrome? {result}")
