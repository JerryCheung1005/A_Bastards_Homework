n = int(input("Enter the number'n': "))
a = int(input("Enter a number in range 1 to 10: "))
c = []
for b in range(1, a):
    print(str(n)*b, end='')
    print("+", end='')
    c.append(int(str(n)*b))

print(str(n)*a, '=', end='')
c.append(int(str(n)*a))
end = int(str(n)*4)
result = sum(c)
print(' ', result)

