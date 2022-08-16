summary_list = []



for csv in [csv_10A1_math, csv_10A2_math, csv_10A3_math]:
    for s in csv:
        s_new = ['', '', '', '', '', '', '', '']
        s_new[0] = s[0]
        s_new[1] = s[1]
        s_new[2] = s[2]
        s_new[3] = s[3] 
        s_new[4] = s[4]
        s_new[5] = s[5]
        summary_list.append(s_new)

for csv in [csv_10A1_math, csv_10A2_math, csv_10A3_math]: 
    
