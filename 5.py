from functools import reduce
from operator import mul

list1 = []
while True:
    num = int(input("Enter a number: "))
    list1.append(num)
    con = str(input("Continue or not: (Yes or No): "))
    if not con.lower() in ("yes"):
        break

print(reduce(mul,list1))