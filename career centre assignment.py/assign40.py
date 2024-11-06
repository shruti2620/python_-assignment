# write python program to unzip a list of tuple into individual lists.

t1_list=[(1,'a'),(2,'b'),(3,'c'),(4,'d'),(5,'e')]
list1,list2=zip(*t1_list)

list1=list(list1)
list2=list(list2)
print("First list:",list1)
print("Second list:",list2)