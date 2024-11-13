"""Question 1 : Is Unique: Implement an algorithm to determine if a string has all unique 
characters. What if you cannot use additional data structures? Hints: #44, #7 7 7, #732"""

def checkUniqueCharacter(s):
    seen_char = set()
    for c in s:
        if c in seen_char:
            return False
        seen_char.add(c)
    return True

input_string = input()
print(checkUniqueCharacter(input_string))

"""If We dont use the additional data structure which is set in this case then we can sort
the string and then check if consecutive character is same then return false """

def checkUniqueness(s):
    p =''.join(sorted(s))
    for i in range(len(p)-1):
        if p[i]==p[i+1]:
            return False
    return True

input_string = input()
print(checkUniqueness(input_string))

"""Analysis of the time Complexity : 
    1.> If we use the set then the time complexity is O(n)
    2.> If we dont use any additional data structure then the sorting causes O(nlogn)
"""
