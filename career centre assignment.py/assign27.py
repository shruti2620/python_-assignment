# write python program to remove duplicates from the list.

"""
there are two ways to remove duplicate element 
1) using of set(): it will remove duplicate element from the list.
2) with logic 

"""
l1=[12,324,56,28,12,56,8,3]
l2=[ ]

for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)