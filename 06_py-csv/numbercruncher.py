# Jackie Zeng
# Cracked
#Soft Dev
# <Processing CSV file with dictionaries and using weighted percentages to select random job>
# 2024-9-19
# Time Spent: 20 minutes
import random
import csv

list1=[]
with open('occupations.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        list1.append(row)
print(list1)
percentage=[]
job=[]
for dict1 in list1:
    percentage.append(float(dict1.get("Percentage")))
#print(percentage)
for dict1 in list1:
    job.append(dict1.get("Job Class"))

print(random.choices(job[1:-1], weights=percentage[1:-1]))