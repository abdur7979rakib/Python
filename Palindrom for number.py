"""string = input(("Enter a string:"))
if(string == string[::-1]):
      print("The string is a palindrome")
else:
      print("The string is not a palindrome")"""

num = int(input("Enter a number:"))
temp = num
rev = 0
while(num>0):
    reminder = num%10
    rev = rev * 10 + reminder
    num = num // 10
if(temp == rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")

