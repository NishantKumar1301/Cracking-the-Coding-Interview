"""
Question 7: Intersection: Given two (singly) linked lists, determine if the two lists intersect.
Return the intersecting node. Note that the intersection is defined based on reference, not value.
That is, if the k-th node of the first linked list is the exact same node (by reference) as the j-th 
node of the second linked list, then they are intersecting.

Observations for solving this question:
1. Intersection is defined based on reference, which means both nodes should point to the exact same memory location to be considered intersecting.
2. Find the length of both linked lists and classify them into shorter and longer lists.
3. Calculate the difference between the lengths of the two linked lists, and skip nodes in the longer list to align both lists.
4. If the ends of the two linked lists do not point to the same node, then the lists are non-intersecting.
5. After the intersecting node, all subsequent nodes in both linked lists must be the same.
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def calculate_length(self, head):
        """
        Calculates the length of a linked list.
        :param head: ListNode, the head of the linked list
        :return: int, the length of the linked list
        """
        length = 0
        while head:
            head = head.next
            length += 1
        return length

    def getIntersectionNode(self, headA, headB):
        """
        Finds the intersection node of two singly linked lists.
        :param headA: ListNode, the head of the first linked list
        :param headB: ListNode, the head of the second linked list
        :return: ListNode, the intersecting node or None if no intersection
        """
        # Calculate the lengths of both lists
        length_A = self.calculate_length(headA)
        length_B = self.calculate_length(headB)

        # Identify the shorter and longer lists
        shorter = headA if length_A < length_B else headB
        longer = headA if length_A >= length_B else headB

        # Advance the pointer for the longer list by the difference in lengths
        difference = abs(length_A - length_B)
        for _ in range(difference):
            longer = longer.next

        # Traverse both lists together until the intersection is found
        while shorter and longer:
            if shorter is longer:
                return shorter
            shorter = shorter.next
            longer = longer.next

        # If no intersection is found
        return None
