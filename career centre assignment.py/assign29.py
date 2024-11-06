# write python program that takes two lists and returns true if they have atleast one common member.

def common_member(list1,list2):
    print(set(list1)&set(list2))

list1= [1,2,3]
list2= [3,4,5]
list3= [6,7,8]
print(common_member(list1,list2))
print(common_member(list2,list3))