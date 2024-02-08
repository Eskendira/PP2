"""Write a Python function that takes a list and returns 
a new list with unique elements of the first list. 
Note: don't use collection set."""

def unielem(ls):
    ls1 = []
    for i in ls:
        if i not in ls1:
            ls1.append(i)
    return ls1

ls = input("enter the nums:")
ls1 = unielem(ls)
print(ls1)