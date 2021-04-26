number = int(input('Enter a number: '))
result = []
for i in range(2, number+1):
    while number % i == 0:

        result.append(i)
        number = number/i


print(result)