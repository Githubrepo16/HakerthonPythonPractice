# Dr. John Wesley has a spreadsheet containing a list of student's IDs,marks,class and name
# Your task is to help Dr. Wesley calculate the average marks of the students.
# Avergae = sum of all marks/total students
# Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet.
# Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won't change.)

from collections import namedtuple
total = int(input("Number : "))
total_marks = 0
for _ in range(total):
    students = namedtuple('student', 'MARKS CLASS NAME ID')
    MARKS, CLASS, NAME, ID = input("Marks,Class,Name,ID : ").split()
    student = students(MARKS, CLASS, NAME, ID)
    total_marks += int(student.MARKS)
avg = total_marks/total
print(avg)

