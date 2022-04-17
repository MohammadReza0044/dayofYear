day=int(input("enter the day of your birthday: "))
month=int(input("enter the month of your birthday: "))
if day>=1 and day<=31:
    if month>=1 and month<=6 :
        print(f" your day of the year is {(month-1)*31+day} ")
    elif month>=7 and month<=12:
        print(f" your day of the year is {(month-1)*30+day+6} ")
    else:
        print("month error")
else:
    print("day error")


print("hello")


