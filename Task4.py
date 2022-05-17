"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from email.mime import nonmultipart

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
marketing = []
nonMarketing = []
all = []
counter = 0
all += texts
all += calls
#to know the breaking point in all array
breakingPoint = len(texts) - 1
test = 0

for numbers in all:
    if counter < breakingPoint:
        if numbers[0] not in nonMarketing:
            nonMarketing.append(numbers[0])
        if numbers[1] not in nonMarketing:
            nonMarketing.append(numbers[1])
    if counter >= breakingPoint:
        if numbers[1] not in nonMarketing:
            nonMarketing.append(numbers[1])
            if numbers[1] in marketing:
                marketing.remove(numbers[1])
        if numbers[0] not in nonMarketing :
            if numbers[0] not in marketing: 
                marketing.append(numbers[0])
    counter += 1

print('These numbers could be telemarketers: ' )
marketing.sort()
for numbers in marketing:
    print(numbers)
