"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
different = []
all = []
all += texts
all += calls

for numbers in all:
    if numbers[0] not in different:
        different.append(numbers[0])
    if numbers[1] not in different:
        different.append(numbers[1])

print('There are ' + len(different) + ' different telephone numbers in the records.')