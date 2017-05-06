p="Y"
while(p=="Y" or p=="y"):
    x = int(input("Enter year? "))
    if(x%4==0):
        if(x%100==0):
            if(x%400==0):
                print("This year is Leap Year")
            else:
                print("This is not Leap Year")
        else:
            print("This is leap Year" )
    else:
        print("This is not Leap Year")
    p = input("Do you want to check again?\n\t\t\tY/N?: ")