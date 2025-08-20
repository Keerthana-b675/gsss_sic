#constructing list into string

list1=['a','b','c','1','2','3']
my_str =''.join(list1)
print(f'str={my_str}')

#constructing string into list
list2=[element for element in my_str]
print(f'list={list2}')