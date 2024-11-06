# write python program to count the number of string where the string length is 2 or more and 
# the first and last character are same from the given list in string.

def count_string(strings):
    count = 0 
    for s in strings:
        if len(s)>=2 and s[0]==s[-1] :
            count+=1
            print(count)

string_list=['121','abc','xyz','123','cba']
print(count_string(string_list))