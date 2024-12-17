"""Question 6 : Sum Lists: You have two numbers represented by a linked list, where each node 
contains a single digit. The digits are stored in reverse order, such that the 1 's digit is at 
the head of the list. Write a function that adds the two numbers and returns the sum as a linked 
list. EXAMPLE Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295. Output: 2 -> 1 -> 9. That is,
912. FOLLOW UP Suppose the digits are stored in forward order. Repeat the above problem. EXAMPLE
Input:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295. Output: 9 -> 1 -> 2. That is, 912"""

#CASE 1: Digits are stored in the reverse order

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    # Function to add two numbers represented by linked list
    def addTwoLists(self, num1, num2):
        # Step 1: Create a dummy linked list to store the result
        dummy = Node(0)
        temp = dummy
        carry = 0
        
        # Step 2: Iterate through both linked lists
        while num1 or num2 or carry:
            result = carry
            # Add num1 data if exists
            if num1:
                result += num1.data
                num1 = num1.next
            # Add num2 data if exists
            if num2:
                result += num2.data
                num2 = num2.next
            
            # Calculate new carry and the current digit
            carry = result // 10
            temp.next = Node(result % 10)  # Create a new node for the current digit
            temp = temp.next 
        
        # Step 3: Return the resulting list
        return dummy.next
    
#Code from line 42-89 is for helper function and to check whether the code is correctly running or not
    
    # Helper function to print the linked list
    def printList(self, head):
        current = head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Helper function to create a linked list from a list of digits
    def createList(self, digits):
        head = None
        for digit in reversed(digits):  # Reversed to create the list in reverse order
            new_node = Node(digit)
            new_node.next = head
            head = new_node
        return head

# Testing the solution with the given test case
def test():
    sol = Solution()

    # Test Case: num1 = 7 -> 1 -> 6 (617), num2 = 5 -> 9 -> 2 (295)
    num1_digits = [7, 1, 6]  # Represents 617
    num2_digits = [5, 9, 2]  # Represents 295
    output = [2, 1, 9]  # Represents 912

    # Create the linked lists for num1 and num2
    num1 = sol.createList(num1_digits)
    num2 = sol.createList(num2_digits)

    # Add the two lists
    result = sol.addTwoLists(num1, num2)

    # Print the result list
    print("Result of Adding Two Lists:")
    sol.printList(result)

# Run the test
test()

#Case 2 : When digits are stored in the forward order

"""
Approach: 
    1.>Reverse both the given linked list 
    2.>Find the sum of the linked list
    3.>Reverse the final result linked list a
    4.>remove the leading zeroes from the result linked list
    eg -> n1 = 6 -> 1 -> 7=(617), reverse = 7-1-6
    n2 = 2 -> 9 -> 5 =(295), reverse = 5-9-2
    sum of both in reverse = 219 = 2-1-9
    reverse of final = 9-1-2 which is final output
"""

class Solution:
    #Function to create a reverse method
    def reverse(self,head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next =prev 
            prev = current
            current = next_node
        return prev
        
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, num1, num2):
        # code here
        #Reverse both the given linked list
        num1 = self.reverse(num1)
        num2 = self.reverse(num2)
        carry = 0
        dummy = Node(0)
        temp = dummy
        #Iterating over both the linked list
        while carry or num1 or num2:
            ans = carry
            if num1:
                ans+=num1.data
                num1=num1.next
            if num2:
                ans+=num2.data
                num2 = num2.next
            carry = ans//10
            temp.next = Node(ans%10)
            temp= temp.next
        #Reverse the final result linked list
        result = self.reverse(dummy.next)
        
        #Remove the leading zero in the final output
        while result and result.data==0:
            result = result.next
                
        # return head of sum list
        return result
        
