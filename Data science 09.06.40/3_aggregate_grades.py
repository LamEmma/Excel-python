import csv  
import os 

# os.mkdir('3_students_grades')

student_summary = open('3_students_grades/students_summary.csv', 'w', newline='', encoding='utf-8-sig')
students_10A1_math = open('2_teacher_filled/10A1_math.csv', 'r', encoding='utf-8', newline='')
students_10A2_math = open('2_teacher_filled/10A2_math.csv', 'r', encoding='utf-8', newline='')
students_10A3_math = open('2_teacher_filled/10A3_math.csv', 'r', encoding='utf-8',newline='')
students_10A1_literature = open('2_teacher_filled/10A1_literature.csv', 'r', encoding='utf-8', newline='')
students_10A2_literature = open('2_teacher_filled/10A2_literature.csv', 'r', encoding='utf-8', newline='')
students_10A3_literature = open('2_teacher_filled/10A3_literature.csv', 'r', encoding='utf-8', newline='')


csv_student_summary = csv.writer(student_summary)
csv_10A1_math = csv.reader(students_10A1_math)
csv_10A2_math = csv.reader(students_10A2_math)
csv_10A3_math = csv.reader(students_10A3_math)
csv_10A1_literature = csv.reader(students_10A1_literature)
csv_10A2_literature = csv.reader(students_10A2_literature)
csv_10A3_literature = csv.reader(students_10A3_literature)

header = ['ID', " Name", ' Class', ' Toán 15p', ' Toán 1 Tiết', ' Toán Cuối Kì', ' Văn 15p', ' Văn 1 Tiết', ' Văn Cuối Kì',' Điểm Trung Bình']

csv_student_summary.writerow(header)



for csv in [csv_10A1_math, csv_10A2_math, csv_10A3_math, csv_10A1_literature,csv_10A2_literature, csv_10A3_literature]:
    next(csv)


summary_list = []

for csv in [csv_10A1_math, csv_10A2_math, csv_10A3_math]:
    for s in csv:
        s_new = ['', '', '', '', '', '', '', '', '']
        s_new[0] = s[0]
        s_new[1] = s[1]
        s_new[2] = s[2]
        s_new[3] = s[3]
        s_new[4] = s[4]
        s_new[5] = s[5]
        summary_list.append(s_new)

for csv in [csv_10A1_literature, csv_10A2_literature, csv_10A3_literature]:
    for s in csv:
        for existing_s_new in summary_list:
            if existing_s_new[0] == s[0]:
                existing_s_new[6] = s[3]
                existing_s_new[7] = s[4]
                existing_s_new[8] = s[5]
                continue 

csv_student_summary.writerows(summary_list)
