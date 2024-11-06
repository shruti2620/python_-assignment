# write python program to add 'in' at the end of given string (length should be at least 3). 
# if given string already ends with 'ing' then add 'ly' instead if the string length of a given string is less than 3,leave it unchanged.

def string(s):
    if len(s)<3:
        print(s)
    elif s.endswith('ing'):
        print(s+'ly')
    else:
        print(s+'in')

print(string("play"))
print(string("playing"))
print(string("go"))