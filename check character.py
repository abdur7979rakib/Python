num = str(input("Enter the Character: "))

if (num>='A' and num<='Z')or(num>='a' and num<='z'):
    print("This character",num,"is an alphabet.")

elif num.isdigit():
    print("This charater",num,"is digit.")

else:
    print("This is the special character.")