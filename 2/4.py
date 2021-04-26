while True:

    string = str(input("Please enter a string: "))
    a = []
    for elements in string:
        a.append(elements)
    b = list(reversed(a))
    if a == b:
        print(True)
    else:
        print(False)


