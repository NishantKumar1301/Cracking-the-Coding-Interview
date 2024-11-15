"""Question6 : String Compression: Implement a method to perform basic string compression using
the counts of repeated characters. For example, the string aabcccccaaa would become a2blc5a3.
If the "compressed" string would not become smaller than the original string, your method should
return the original string. You can assume the string has only uppercase and lowercase 
letters (a - z)."""

def string_compression(input_string):
    count = 1
    compressed=[]
    for i in range(len(input_string)-1):
        if input_string[i]==input_string[i+1]:
            count+=1
        else:
            compressed.append(input_string[i]+str(count))
            count =1

    compressed.append(input_string[-1]+str(count))
    compressed_string = ''.join(compressed)
    return compressed_string if len(compressed_string)<len(input_string) else input_string

input_string = input()
print(string_compression(input_string))