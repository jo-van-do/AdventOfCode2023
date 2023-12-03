# Open data
with open('AdventOfCode2023\Day 1\data1.1.txt', 'r') as f:
    lines = f.read().split('\n')
f.close()

# Function for reversing
def reverse_slicing(s):
    return s[::-1]

# Prepare for-loop
digits = ['0','1','2','3','4','5','6','7','8','9']
digits_written = ['zero','one','two','three','four','five','six','seven','eight','nine']

total = 0

# Get digits and add them together
for line in lines:

    line_numbers = {}

    # pair digits with indices
    for i,char in enumerate(line):
        if char in digits:
            line_numbers[i] = char
     
    # pair written numbers with indices
    for n in digits_written:
        if n in line:
            d = str(digits_written.index(n)) # turn into digit string
            line_numbers[line.index(n)] = d
    
    # check written numbers from back of list
    r_line = line[::-1] 

    for n in digits_written:
        r_n = n[::-1] # check for backwards written number from back of the list

        if r_n in r_line:
            d = str(digits_written.index(n)) # turn into digit string
            ind = len(line) - 1 - r_line.index(r_n) # get correct index
            line_numbers[ind] = d
            

    nmbrs = sorted(line_numbers.items()) # sort on digit index
    number = nmbrs[0][-1]+nmbrs[-1][-1] # get the digit from the first and last registered index and concatenate 
    
    total += int(number)

print(total)


