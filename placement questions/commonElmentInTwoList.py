#common element betwwwn two lists
list1=[1,2,3,4,5]
list2=[4,5,6,7,8]
set1=set(list1)
set2=set(list2)
common_set=set1&set2
print(common_set)
common_elements=list(common_set)
print(common_elements)