# Jackie Zeng
# China Rats plus One
# Soft Dev
# <parse/python dictionaries and parsing/opens text file and splits the data and then appends a dictionary of the split data>
#Time spent: ~20 minutes
import random

krewes_list = []

with open('krewes.txt', 'r') as file:
    content = file.read().strip()


entries = content.split('@@@')


for entry in entries:
    details = entry.split('$$$')
    if len(details) == 3:
        period, devo, ducky = details
        krewes_list.append({'period': period, 'devo': devo, 'ducky': ducky})

selected_devo = random.choice(krewes_list)

print(selected_devo)