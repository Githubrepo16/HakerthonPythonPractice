# The provided code stub reads two integers,  and , from STDIN.
# Add logic to print two lines.
# The first line should contain the result of integer division,  // .
# The second line should contain the result of float division,  / .
# No rounding or formatting is necessary.

def task_two():
    a = int(input("Enter First Number : "))
    b = int(input("Enter Second Number : "))

    print("integer division =", a // b)
    print("float division =", a / b)


task_two()