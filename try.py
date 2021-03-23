from functools import reduce
from operator import mul
list1=[11,5,17,18,23]
list1=map(str, list1)
list2=list(map(len,list1))
print(list2)