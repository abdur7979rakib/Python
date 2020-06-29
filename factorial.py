def fact(n):
    f = 1
    for i in range (1, n+1):
        f = f*i
    return f

x = int(input("Enter the number: "))
result = fact(x)
print(result)



"""n = int(input("Enter the number: "))
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print( "The factorial of", n , "is : ", end="")
print(fact)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))

"""