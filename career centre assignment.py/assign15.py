# write python program to get single string from two given string, seperated by a space and swap the first two character of each string.


def swap_and_join_string (str1,str2):
   new_str1 = str2[:2]+str1[2:]
   new_str2 = str1[:2]+str1[2:]
   result = new_str1 + " " + new_str2


str1 = "hello"
str2 = "python"
result = (str1,str2)
print(result)