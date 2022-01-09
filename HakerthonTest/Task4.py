# Given a year, determine whether it is a leap year.
# If it is a leap year, return the Boolean True, otherwise return False.
# Note that the code stub provided reads from STDIN and passes arguments to the is_leap function.
# It is only necessary to complete the is_leap function.
# In the Gregorian calendar, three conditions are used to identify leap years:
# The year can be evenly divided by 4, is a leap year, unless
# The year can be evenly divided by 100, it is NOT a leap year, unless
# The year is also evenly divisible by 400. Then it is a leap year.
# This means that in the Gregorian calendar,
# the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years
# Given a year, determine whether it is a leap year.
# If it is a leap year, return the Boolean True, otherwise return False.
a = int(input("Enter a year(YYYY) : "))
def task_four():

    leap = False
    if a % 4 == 0:
        if a % 100 == 0:
            if a % 400 == 0:
                leap = "Leap Year", a % 4, a % 100, a % 400, True
            else:
                leap = "Not a Leap Year", a % 4, a % 100, a % 400, False
        else:
            leap = "Leap Year", a % 4, a % 100, a % 400, True
    else:
        leap = "Not a Leap Year", a % 4, a % 100, a % 400, False
    return leap


#     print("Leap Year", 2000 % 4, 2000 % 100, 2000 % 400) # ('Leap Year', 0, 0, 0, True)
#     print("Not a Leap Year", 2100 % 4, 2100 % 100, 2100 % 400) # ('Not a Leap Year', 0, 0, 100, False)
#     print("Leap Year", 2400 % 4, 2400 % 100, 2400 % 400) # ('Leap Year', 0, 0, 0, True)
#     print("Not a Leap Year", 3455 % 4, 3455 % 100, 3455 % 400) # ('Not a Leap Year', 3, 55, 255, False)
#     print("Not a Leap Year", 1990 % 4, 1990 % 100, 1990 % 400) # ('Not a Leap Year', 2, 90, 390, False)
#     print("Leap Year",1992 % 4, 1992 % 100, 1992 % 400) # ('Leap Year', 0, 92, 392, True)
# task_four()
print(task_four())

