import csv
import os

# os.mkdir('average_grades')

average_grades = open('average_grades/average_grades.csv', 'w', encoding='utf-8-sig', newline='')
students_summary = open('3_students_grades/students_summary.csv', 'r', encoding='utf-8-sig')


csv_average = csv.writer(average_grades)
csv_summary_students = csv.reader(students_summary)
header = next(csv_summary_students)


header = ['ID', " Name", ' Class', ' Toán 15p', ' Toán 1 Tiết', ' Toán Cuối Kì', ' Văn 15p', ' Văn 1 Tiết', ' Văn Cuối Kì',' Điểm Trung Bình','Rank']

csv_average.writerow(header)

summary_average = []

for s in csv_summary_students:
    s_new = ['','', '', '', '', '', '', '', '','','']
    for i in range(9):
        s_new[i] = s[i]
    average = round((float(s[3]) + float(s[4]) + float(s[5]))/3,2)
    s_new[9] = average
    summary_average.append(s_new)
    rank = ''
    if average >=8.0:
        rank = 'Giỏi'
    if average >=6.5 and average < 8.0:
        rank ='Tiên tiến'
    else: 
        rank ='Trung bình'
    s_new[10] = rank 
    


csv_average.writerows(summary_average)
