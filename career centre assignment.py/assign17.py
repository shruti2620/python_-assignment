# write python function to reverse a string if its length is multiple of 4.

def string_multiple_of_four(s):
    if len(s)%4 ==0:
        print(s[0:-1])
    else:
        print(s)

print(string_multiple_of_four("hello"))
print(string_multiple_of_four("python"))
print(string_multiple_of_four("good"))
print(string_multiple_of_four("abcd"))