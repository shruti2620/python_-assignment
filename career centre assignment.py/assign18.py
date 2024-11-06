# write python program to get a string made of te first 2 and last 2 character from the given string.
# if the string length is less than 2, return instead of the empty string.

def first_and_last_two(s):
    if len(s)<2:
        print()
    else:
        print(s[:2] + s[-2:])

print(first_and_last_two("python"))
print(first_and_last_two("good"))
print(first_and_last_two("morning"))

