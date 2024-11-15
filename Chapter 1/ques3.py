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

#Second Approach

def urilify_string(input_string):
    true_length = len(input_string.rstrip())
    input_string=list(input_string)
    space_count = sum(1 for i in range(true_length) if input_string[i]==" ")
    index = true_length + space_count*2
    for i in range(true_length-1,-1,-1):
        if input_string[i]==' ':
            input_string[index-3:index]="%20"
            index -=3
        else:
            input_string[index-1]=input_string[i]
            index-=1
    return ''.join(input_string)
input_string=input()
print(urilify_string(input_string))