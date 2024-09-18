# Jackie Zeng
# China Rats plus One
# Soft Dev
# <parse/python dictionaries and parsing/opens text file and splits the data and then appends a dictionary of the split data>
#Time spent: ~20 minutes
import random

krewes_list = []

with open('krewes.txt', 'r') as file:
    content = file.read().strip() #string of data


entries = content.split('@@@') #make list of each person's details
 

for entry in entries: #for each of one person's detail make list for specific detail of name, pd, ducky
    details = entry.split('$$$')
    if len(details) == 3:
        period, devo, ducky = details
        krewes_list.append({'period': period, 'devo': devo, 'ducky': ducky}) #add dictionary to list 

selected_devo = random.choice(krewes_list) #picks random devo from list

print(selected_devo)
