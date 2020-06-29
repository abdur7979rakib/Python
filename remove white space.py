test = "Python is    the       best."
print("The original string is : " + test)
x = " ".join(test.split())
print("The strings after extra space removal : " + str(x))
