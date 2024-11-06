# write python program to check whether a list contain a sub list.

def contain(main_list,sub_list):
        for i in range(len(main_list)-len(sub_list)+1):
                if main_list[i:i+len(sub_list)]==sub_list:
                        print(True)
                else:
                        print(False)

main_list=[1,2,3,4,5,6]
sub_list=[4,5]
result=contain(main_list,sub_list)
print(result)
    
