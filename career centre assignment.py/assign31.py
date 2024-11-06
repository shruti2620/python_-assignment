# write python function that takes a lists and returns a new list with unique elements of the first list.

def unique_element(input_list):
    unique_list=list(set(input_list))
    print(unique_list)

input_list= [1,3,2,4,5,6,5,6,5,6,7,8,9,9,1,2,3]
unique_list=(unique_element(input_list))
print("Unique_element:",unique_list)
