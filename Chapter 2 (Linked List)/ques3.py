"""Question3: Delete Middle Node: Implement an algorithm to delete a node in the middle 
(i.e., any node but the first and last node, not necessarily the exact middle) of a singly 
linked list, given only access to that node. EXAMPLE Input:the node c from the linked list 
a->b->c->d->e->f Result:The new linked list looks like a->b->d->e->f"""

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


def findMiddleNode(head):
    """
    Finds the middle node of the linked list.
    :type head: Node
    :rtype: Node
    Implement your logic here.
    """
    slow = fast = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next 
        slow = slow.next 
    return slow


def deleteMiddleNode(head):
    """
    Finds and deletes the middle node of the linked list.
    :type head: Node
    :rtype: Node
    Implement your logic here.
    """
    middle_element = findMiddleNode(head)
    current =previous = head
    while current is not None:
        if current == middle_element:
            previous.next = current.next
        else:
            previous=current
        current = current.next
    return head


# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    values = [x for x in input("Enter linked list values separated by space: ").split()]
    for value in values:
        ll.append(value)

    print("Original Linked List:")
    print(ll)

    ll.head = deleteMiddleNode(ll.head)  # Delete the middle node and update the head if necessary
    print("Updated Linked List after deleting the middle node:")
    print(ll)
