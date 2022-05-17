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

allTheCalls = {}
theLongestCall = 0
theLongestNumber = ''

for numbers in calls:
    if numbers[0] not in allTheCalls:
        allTheCalls[numbers[0]] = int(numbers[3])
        if allTheCalls[numbers[0]] >= theLongestCall:
            theLongestCall = allTheCalls[numbers[0]]
            theLongestNumber = numbers[0]
    else:
        allTheCalls[numbers[0]] = int(allTheCalls[numbers[0]]) + int(numbers[3])
        if allTheCalls[numbers[0]] >= theLongestCall:
            theLongestCall = allTheCalls[numbers[0]]
            theLongestNumber = numbers[0]

    if numbers[1] not in allTheCalls:
        allTheCalls[numbers[1]] = int(numbers[3])
        if allTheCalls[numbers[1]] >= theLongestCall:
            theLongestCall = allTheCalls[numbers[1]]
            theLongestNumber = numbers[1]
    else:
        allTheCalls[numbers[1]] = int(allTheCalls[numbers[1]]) + int(numbers[3])
        if allTheCalls[numbers[1]] >= theLongestCall:
            theLongestCall = allTheCalls[numbers[1]]
            theLongestNumber = numbers[1]

print( theLongestNumber +' spent the longest time, '+ str(theLongestCall) + ' seconds, on the phone during September 2016.')