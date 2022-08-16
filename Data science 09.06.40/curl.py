import os 
import csv 
# students = open('students.csv', 'r', encoding='utf-8-sig')

students = open('students.csv', 'r', encoding='utf-8-sig')

students_10A1_math = open('1_teacher_unfilled/10A1_math.csv', 'w', encoding='utf-8', newline='')
students_10A2_math = open('1_teacher_unfilled/10A2_math.csv', 'w', encoding='utf-8', newline='')
students_10A3_math = open('1_teacher_unfilled/10A3_math.csv', 'w', encoding='utf-8',newline='')
students_10A1_literature = open('1_teacher_unfilled/10A1_literature.csv', 'w', encoding='utf-8', newline='')
students_10A2_literature = open('1_teacher_unfilled/10A2_literature.csv', 'w', encoding='utf-8', newline='')
students_10A3_literature = open('1_teacher_unfilled/10A3_literature.csv', 'w', encoding='utf-8', newline='')

csv_students = csv.reader(students)

csv_10A1_math = csv.writer(students_10A1_math)
csv_10A2_math = csv.writer(students_10A2_math)
csv_10A3_math = csv.writer(students_10A3_math)
csv_10A1_literature = csv.writer(students_10A1_literature)
csv_10A2_literature = csv.writer(students_10A2_literature)
csv_10A3_literature = csv.writer(students_10A3_literature)


header_math = ['ID', " Name", ' Class', ' Toán 15p', ' Toán 1 Tiết', ' Toán Cuối Kì']
header_math = ['ID', " Name", ' Class', ' Văn 15p', ' Văn 1 Tiết', ' Văn Cuối Kì']

for csv in [csv_10A1_math, csv_10A2_math, csv_10A3_math]:
    csv.writerow(header_math)

for csv in [csv_10A1_literature, csv_10A2_literature, csv_10A3_literature]:
    csv.writerow(header_math)   

for s in csv_students:
    if s[2] == '10A1':
        csv_10A1_math.writerow(s)
        csv_10A1_literature.writerow(s)
    if s[2] == '10A2':
        csv_10A2_math.writerow(s)
        csv_10A2_literature.writerow(s) 
    if s[2] == '10A3':
        csv_10A3_math.writerow(s)
        csv_10A3_literature.writerow(s)
