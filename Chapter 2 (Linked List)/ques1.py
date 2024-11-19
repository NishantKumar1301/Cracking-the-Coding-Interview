"""Question1 : Remove Dups! Write code to remove duplicates from an unsorted linked list. 
FOLLOW UP How would you solve this problem if a temporary buffer is not allowed? 
"""
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


# Method 1: Using a buffer (e.g., set()) = Time Complexity =O(n^2) Space Complexity =O(n)
def deleteDuplicate(head):
    """
    :type head: Node
    :rtype: Node
    Remove duplicates from the linked list using extra memory.
    """
    unique_set = set()
    current = head
    previous =None
    while current is not None:
        if current.value in unique_set:
            previous.next = current.next 
        else:
            unique_set.add(current.value)
            previous = current
        current = current .next 
    return head


# Method 2: Without using a buffer = Time Complexity = O(n) Space Complexity = O(1)
def deleteDuplicateNoBuffer(head):
    """
    :type head: Node
    :rtype: Node
    Remove duplicates from the linked list without using extra memory.
    """
    current = head
    while current is not None:
        temp = current 
        while temp.next is not None:
            if temp.next.value == current.value:
                temp.next = temp.next.next 
            else:
                temp = temp.next 
        current = current.next 
    return head    


# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    values = [int(x) for x in input("Enter linked list values separated by space: ").split()]
    for value in values:
        ll.append(value)

    print("Original Linked List:")
    print(ll)

    ll.head = deleteDuplicate(ll.head)  # Remove duplicates using a buffer
    print("Linked List after removing duplicates using a buffer:")
    print(ll)

    #Recreate the linked list for the second method
    ll = LinkedList()
    for value in values:
        ll.append(value)

    ll.head = deleteDuplicateNoBuffer(ll.head)  # Remove duplicates without a buffer
    print("Linked List after removing duplicates without a buffer:")
    print(ll)
