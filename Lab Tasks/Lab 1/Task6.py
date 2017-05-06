x = input("Enter a String: ")
i=0
j=0
for a in x:
    if a.isdigit():
        i=i+1
    elif a.isalpha():
        j=j+1

print("Number of Letters: ",j)
print("Number of Digits: ",i)