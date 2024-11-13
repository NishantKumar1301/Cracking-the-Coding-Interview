"""Question3 : URLify: Write a method to replace all spaces in a string with '%20'.
You may assume that the string has sufficient space at the end to hold the additional 
characters, and that you are given the "true" length of the string. (Note: If implementing 
in Java, please use a character array so that you can perform this operation in place.) 
EXAMPLE Input: Output: "Mr John Smith "Mr%20John%20Smith" Hints: #53, # 118"""

def urlify(s):
    s = s.strip()
    ans = []
    for char in s:
        if char==" ":
            ans.append("%20")
        else:
            ans.append(char)
    return "".join(ans)

input_string=input()
print(urlify(input_string))