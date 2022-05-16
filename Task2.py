"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

theLongest = 0
index = 0
counter = 0
for number in calls:
    if int(number[3]) >= theLongest:
        theLongest = int(number[3])
        index = counter
    counter += 1

print(calls[index][0] + ' spent the longest time, ' + str(theLongest) + ' seconds, on the phone during September 2016.')