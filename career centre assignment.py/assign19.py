# write python function to insert a string in the middle of the string.

def insert_in_middle(original,to_insert):
    middle_index=len(original)//2
    print(original[:middle_index] + to_insert + original[middle_index:])

print(insert_in_middle("hello","python"))
print(insert_in_middle("good","morning"))
print(insert_in_middle("hello","ahemdabad"))