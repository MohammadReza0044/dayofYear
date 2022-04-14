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



# day=int(input("enter the day of your birthday: "))
# month=int(input("enter the month of your birthday: "))
# year=int(input("enter the year of your birthday: "))
# if year<=1401:
#     if month>0 and month<=12:
#         if day>=1 and day<=31:
#             print(f"you are {(1401-year)-1} year and {round(((month-1)*31+day)/31)} month and {((month-1)*31+day)%31} day.")
#         elif month>=7 and month<=12:
#             print(f"you are {1401-year} year and {12-month} month and {(month-1)*31+day+6} day.")
#         else:
#             print("day error")
#     else:
#         print("month eror")
# else:
#     print("year error")

print(22%7)

