"""Question9: String Rotation:Assume you have a method isSubstring which checks if one word is a 
substring of another. Given two strings, sl and s2, write code to check if s2 is a rotation
of sl using only one call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat")."""

def contains_substring(str1, str2):
    return str2 in str1

def is_string_rotation(original_str, rotated_str):
    if len(original_str) != len(rotated_str):
        return False
    
    return contains_substring(original_str + original_str, rotated_str)

first_string = input("Enter the first string: ")
second_string = input("Enter the second string: ")

if is_string_rotation(first_string, second_string):
    print(f'"{second_string}" is a rotation of "{first_string}".')
else:
    print(f'"{second_string}" is NOT a rotation of "{first_string}".')
