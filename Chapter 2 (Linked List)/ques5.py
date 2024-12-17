"""Question5 : Partition: Write code to partition a linked list around a value x, such that all
nodes less than x come before all nodes greater than or equal to x. If xis contained within the 
list, the values of x only need to be after the elements less than x (see below). The partition 
element x can appear anywhere in the "right partition"; it does not need to appear between the
left and right partitions. EXAMPLE Input: Output: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5] 
3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8"""

#Similar Question On Leetcode : https://leetcode.com/problems/partition-list/

""" 
Approach:
        1.>Take two linked list small_linked_list and large_linked_list
        2.>Traverse through the given linked list
        3.>If the  current value is less than given value x then add the given node to the small_linked_list
        4.> Else add it to the larger_linked_list
        5.>Combine both the smaller and larger linked list
        6.>Return the smaller_linked_list
""" 

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        
        #Step1: Creation of both the smaller and larger linked list
        smaller_linked_list = ListNode(0)
        larger_linked_list = ListNode(0)
        
        #Step2: Take 2 pointer small and large to take track o both the linked list
        small = smaller_linked_list
        large = larger_linked_list
        
        #Step3: Traverse through the linked list
        while head is not None:
            #Step4: put the head value in the proper linked list
            if head.val<x:
                small.next = head
                small = small.next 
            else:
                large.next = head
                large = large.next 
            
            head = head.next 
        
        #Step4: Combine both the smaller and larger linked list
        large.next = None
        small.next = larger_linked_list.next 
        
        #Step5: Return the next value of smaller linked list
        return smaller_linked_list.next
        
