"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from operator import indexOf

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
areaCodes = []
callers = 0
receivers = 0

for numbers in calls:
  if numbers[0][slice(5)] == '(080)':
    callers += 1
    if numbers[1][slice(2)] == '(0':
      if numbers[1][slice(indexOf(numbers[1],')') + 1)] not in areaCodes:
        areaCodes.append(numbers[1][slice(indexOf(numbers[1],')') + 1)])
    if numbers[1][slice(3)] == '140' and '140' not in areaCodes:
      areaCodes.append('140')
    if numbers[1][slice(1)] == '7':
      if numbers[1][slice(4)] not in areaCodes:
        areaCodes.append(numbers[1][slice(4)])
    if numbers[1][slice(1)] == '8':
      if numbers[1][slice(4)] not in areaCodes:
        areaCodes.append(numbers[1][slice(4)])
    if numbers[1][slice(1)] == '9':
      if numbers[1][slice(4)] not in areaCodes:
        areaCodes.append(numbers[1][slice(4)])
    if numbers[1][slice(5)] == '(080)':
      receivers +=  1

print('The numbers called by people in Bangalore have codes: ')
areaCodes.sort()
for areas in areaCodes:
  print(areas)

rounding = round((receivers / callers) * 100, 2)
print(str(rounding) + ' percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.')