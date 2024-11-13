"""Question2 : Check Permutation: Given two strings, write a method to decide if one is a
permutation of the other. Hints: #7, #84, #722, #737"""

def check_permutation(s1,s2):
    if len(s1)!=len(s2):
        return False
    
    char_dict={}
    
    for c in s1:
        if c in char_dict:
            char_dict[c]+=1
        else:
            char_dict[c]=1
    
    for c in s2:
        if c in char_dict:
            char_dict[c]-=1
        else:
            return False
    
    for count in char_dict.values():
        if count!=0:
            return False
    
    return True

s1 = input()
s2 = input()
print(check_permutation(s1,s2))

"""Time Complexity Analysis: O(n) where n is the length of the string"""