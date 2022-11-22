import csv
from array import array
from itertools import count


#Questions 1. load the dataset csv file as a list of lines using Python
with open('ds_salaries.csv',newline="") as f1:
    reader1 = csv.DictReader(f1)

    for row in reader1:
        print (row)


#Questions 2. compute average salary by year?
with open('ds_salaries.csv',newline="") as f2:
    reader2 = csv.DictReader(f2)
    sum=0
    for row in reader2:
        #print (row)
        if (row["work_year"]=="2020"):
            sum=sum+int(row["salary"])
    print (sum)
# salary=[]
# year2020=0
# year2021=0
# year2022=0

# for i in csvreader:
#     salary.append(i[5])
#     if(i[1]=='2020'):
#         year2020=year2020+int(i[5])
#     elif(i[1]=='2021'):
#         year2021=year2021+int(i[5])
#     elif(i[1]=='2022'):
#         year2022=year2022+int(i[5])
# del salary[0]
# sum=0
# for i in salary:
#     sum=sum+int(i)

# #print(year2020,year2021,year2022)

    
# print ("The average of salary is:",sum/len(salary))