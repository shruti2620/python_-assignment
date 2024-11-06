# write python program to check a list is empy or not.

def list_empty_or_not(my_list): 
    print(len(my_list) == 0)

l1=[1,3,5,7,9]
l2=[]
print(list_empty_or_not(l1))
print(list_empty_or_not(l2))