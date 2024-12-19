"""QUESTION 8: Loop Detection: Given a circular linked list, implement an algorithm that returns the
node at the beginning of the loop. DEFINITION Circular linked list: A (corrupt) linked list in which
a node's next pointer points to an earlier node, so as to make a loop in the linked list. 
EXAMPLE Input: A -> B -> C -> D -> E -> C [the same C as earlier] Output: C"""

"""Approach:
    1.>Take 2 pointers slow and fast  which points to the head initially
    2.>Loop Through the linked list and do the following operations
    3.>Move the slow pointer by 1 place and fast by 2 place
    4.>If slow == fast then loop is found
    5.>Now find the node of the beginning of the linked list
"""

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
        

def detect_cycle_start(head):
    if not head or not head.next:
        return None 
    #Take 2 pointer slow and fast
    slow,fast = head,head
    
    #Detect the loop  by iterating over the linked list
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next 
        
        if slow == fast: #Cycle Detected
            break 
    else:
        return None #No Cycle detected

    #Find the start node of the cycle 
    slow = head 
    while slow != fast:
        slow = slow.next 
        fast = fast.next
        
    return slow 


#Example Usage : 
head = ListNode("A")
nodeB = ListNode("B")
nodeC = ListNode("C")
nodeD = ListNode("D")
nodeE = ListNode("E")

head.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
nodeE.next = nodeC  # Creating the loop

start_of_cycle = detect_cycle_start(head)
if start_of_cycle:
    print("Cycle starts at node:", start_of_cycle.value)
else:
    print("No cycle detected.")
        
