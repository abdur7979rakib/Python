
n = int(input("Enter Number: "))
average = 0
sum = 0
for num in range(0,n+1,1):
    sum = sum+num
average = sum / n
print("The sum is: ",sum)
print("Average of first", n, "natural number is: ", average)