def fact(n):
    if n<=1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))


#Task 2 

import math
num=float(input("Enter a number: "))
Square_root=math.sqrt(num)
Logarithm=math.log(num)
Sine=math.sin(num)
print("Square root of",num,"is",Square_root)
print("Logarithm of",num,"is",Logarithm)
print("Sine of",num,"is",Sine)
