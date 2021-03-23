list1 = []
while True:
    num = int(input("Enter a number: "))
    list1.append(num)
    con = str(input("Continue or not: (Yes or No): "))
    if not con.lower() in ("yes"):
        break

list1=map(str, list1)
list2=list(map(len,list1))
print(list2)