import os 
import csv 
import random 


# os.mkdir('2_teacher_unfilled')


students = open('students.csv', 'r', encoding='utf-8-sig')
students_10A1_math = open('2_teacher_filled/10A1_math.csv', 'w', encoding='utf-8', newline='')
students_10A2_math = open('2_teacher_filled/10A2_math.csv', 'w', encoding='utf-8', newline='')
students_10A3_math = open('2_teacher_filled/10A3_math.csv', 'w', encoding='utf-8',newline='')
students_10A1_literature = open('2_teacher_filled/10A1_literature.csv', 'w', encoding='utf-8', newline='')
students_10A2_literature = open('2_teacher_filled/10A2_literature.csv', 'w', encoding='utf-8', newline='')
students_10A3_literature = open('2_teacher_filled/10A3_literature.csv', 'w', encoding='utf-8', newline='')


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
    random_math = [s[0], s[1], s[2]]
    random_math.append(round(random.uniform(4,10),1))
    random_math.append(round(random.uniform(4,10),1))
    random_math.append(round(random.uniform(4,10),1))

    random_literature =[s[0], s[1], s[2]] 
    random_literature.append(round(random.uniform(4,10),1))
    random_literature.append(round(random.uniform(4,10),1))
    random_literature.append(round(random.uniform(4,10),1))

    if s[2] == '10A1':
        csv_10A1_math.writerow(random_math)
        csv_10A1_literature.writerow(random_literature)
    if s[2] == '10A2':
        csv_10A2_math.writerow(random_math)
        csv_10A2_literature.writerow(random_literature) 
    if s[2] == '10A3':
        csv_10A3_math.writerow(random_math)
        csv_10A3_literature.writerow(random_literature)
