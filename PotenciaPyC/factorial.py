# def fact(n, f):
#     if n == 1:
#         return f
#     else:
#         return fact(n -1 , f * (n - 1))

# num = int(input("Ingrese el número para hallar su factorial: "))
# factorial = fact(num, num)
# print(factorial)


from math import factorial

num = int(input("Ingrese el número para hallar su factorial: "))

fac = factorial(num)
print(fac)
