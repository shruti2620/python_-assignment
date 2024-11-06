# write python program to find the second smallest number in a list.

def second_smallest(number):
    unique_number= sorted(set(number))
    if len(unique_number)>2:
        print(None)
        print(unique_number[1])

number=[1,2,3,4,5,6,7,8,9,8,6,4,2]
second_smallest= second_smallest(number)
print(second_smallest)