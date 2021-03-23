from operator import mul

vector1 = eval(input("Enter the first vector:"))
vector2 = eval(input("Enter the second vector:"))

print(sum(map(mul,vector1,vector2)))