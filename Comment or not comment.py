n = str(input("Enter the comment: "))
for i in range(len(n)):
    if (((n[i]=='/') and (n[i+1]=='/')) or (n[i]=='#')):

        print("comment")
        break
    else:
        print("Not comment")
        break


