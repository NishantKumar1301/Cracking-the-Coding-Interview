"""Question5: One Away: There are three types of edits that can be performed on strings:
insert a character, remove a character, or replace a character. Given two strings,
write a function to check if they are one edit (or zero edits) away. 
EXAMPLE pale, ple -> true pales, pale -> true pale, bale -> true pale, bake -> false 
Hints:#23, #97, #130"""

def oneWay(s1,s2):
    if abs(len(s1)-len(s2))>1:
        return False

    if len(s1)==len(s2):
        diff =0 
        for i in range(len(s2)):
            if(s1[i]!=s2[i]):
                diff+=1
                if diff >1:
                    return False
        
        return diff<=1

    if len(s1)+1==len(s2):
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                return s1[i:]==s2[i+1:]
        return True
    

    if len(s1)==len(s2)+1:
        for i in range(len(s2)):
            if s1[i]!=s2[i]:
                return s1[i+1:]==s2[i:]
        
        return True

    return False

str1 = input()
str2 = input()
print(oneWay(str1,str2))