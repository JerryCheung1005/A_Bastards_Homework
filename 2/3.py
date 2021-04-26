import random

number = []
n = int(input("How many people play this game?  "))
for i in range(n):
    number.append(i)

for r in range(len(number) - 1):
    length = int(len(number))
    quit = random.randint(0, length-1)
    del number[quit]
    length = length - 1

print(number)

