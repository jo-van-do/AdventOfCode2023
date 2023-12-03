# Open data
with open('AdventOfCode2023\Day 1\data1.1.txt', 'r') as f:
    lines = f.read().split('\n')
f.close()

lines.pop()

# Prepare for-loop
digits = ['0','1','2','3','4','5','6','7','8','9']
digits_written = ['zero','one','two','three','four','five','six','seven','eight','nine']

total = 0

# Get digits and add them together
for line in lines:

    line_numbers = {}

    # pair digits with indices
    for char in line:
        if char in digits:
            line_numbers[line.index(char)] = char
     
    # pair written numbers with indices
    for n in digits_written:
        if n in line:
            d = str(digits_written.index(n)) # turn into digit string
            line_numbers[line.index(n)] = d

    nmbrs = sorted(line_numbers.items()) # sort on digit index
    number = nmbrs[0][-1]+nmbrs[-1][-1] # get the digit from the first and last registered index and concatenate 

    total += int(number)

print(total)
