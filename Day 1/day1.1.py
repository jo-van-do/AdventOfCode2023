# Open data
with open('AdventOfCode2023\Day 1\data1.1.txt', 'r') as f:
    lines = f.read().split('\n')
f.close()

# Prepare for-loop
digits = ['0','1','2','3','4','5','6','7','8','9']
number = ''
total = 0

# Get digits and add them together
for line in lines:
    for char in line:
        if char in digits:
            number = char
            break
    for char in reversed(line):
        if char in digits:
            number += char
            break
    total += int(number)

print(total)


