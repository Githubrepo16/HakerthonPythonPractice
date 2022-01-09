# The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:
# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the multiplication of the two numbers.

def task_one():
    a = int(input("Enter First Number : "))
    b = int(input("Enter Second Number : "))

    print("sum =", a + b)
    print("difference =", a - b)
    print("mul =", a * b)

task_one()