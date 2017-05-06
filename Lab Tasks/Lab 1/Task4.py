p="y";
while(p == "y" or p == "Y"):
    x = int(input("Enter the Month Number: "))
    if(x>=2 and x<=3):
        print("The Autumn Season is in Progression")
    if (x >= 4 and x <= 5):
        print("The Spring Season is in Progression")
    if(x>=6 and x<=9):
        print("The Summer Season is in Progression")
    if(x>=10 or x==1):
        print("The Winter Season is in Progression")
    p = input("Do you want to check again?\n\t\t\tY/N?: ")