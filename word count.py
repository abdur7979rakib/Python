str = "Python is the easiest language in the world"
count = 1
for i in range(len(str)):
    if (str[i] == ' ' and (i+1)!= ' '):
        count += 1
print(count)

"""string = "Python is the easiest  Language"
x = len(string.split())
print(x)"""
