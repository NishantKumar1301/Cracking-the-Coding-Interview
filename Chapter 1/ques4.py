""" Question4:Palindrome Permutation: Given a string, write a function to check if it is a 
permutation of a palindrome. A palindrome is a word or phrase that is the same forwards
and backwards. A permutation is a rearrangement of letters. The palindrome does not need to 
be limited to just dictionary words. EXAMPLE Input: Output: Tact Coa True 
(permutations: "taco cat", "atco eta", etc.) Hints: #106, #121, #134, #136
"""

from collections import Counter

def palindromePermutation(s):
    s = "".join(c.lower() for c in s if c.isalpha())
    char_dict =Counter(s)
    
    odd_count=0
    
    for c in char_dict.values():
        if c%2 !=0:
            odd_count+=1
        
    return odd_count<=1

input_string = "taco cat"
print(palindromePermutation(input_string))