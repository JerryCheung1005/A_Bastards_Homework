"""Enter numbers until execute 'No' demand."""
list1 = []

while True:
    num = int(input("Enter a number: "))
    list1.append(num)
    con = str(input("Continue or not: (Yes or No): "))
    if not con.lower() in ("yes"):
        break
total = sum(list1)
length = len(list1)
result = total / length
Avg3 = round(result, 3)
print("The average number of the list is", Avg3)