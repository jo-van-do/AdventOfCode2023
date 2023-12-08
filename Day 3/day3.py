import numpy as np
from string import punctuation


# Functions

def isNumber(char):
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    if char in numbers:
        return True
    
    return False

def containsSymbol(env):
    symbols = list(punctuation)
    symbols.remove('.')
    for symbol in symbols:
        if symbol in env:
            return True
    
    return False

def isStar(char):
    if char == '*':
        return True
    
    return False

def scanTopEnvironment(matrix, row, column):
    if row == 0:
        top_env = []
    elif column == 0:
        top_env = matrix[row-1][column:column+2]
    else:
        top_env = matrix[row-1][column-1:column+2]
    
    return top_env

def scanBottomEnvironment(matrix, row, column):
    if row == len(matrix) -1 :
        bottom_env = []
    elif column == 0:
        bottom_env = matrix[row-1][column:column+2]
    else:
        bottom_env = matrix[row+1][column-1:column+2]
        
    return bottom_env

def scanSideEnvironment(matrix, row, column):
    
    if column == 0:
        left_side = ''
        right_side = matrix[row][column+1]
    elif column == len(matrix) -1:
        left_side = matrix[row][column-1]
        right_side = ''
    else:
        left_side = matrix[row][column-1]
        right_side = matrix[row][column+1]
        
    side_env = [left_side, right_side]
    
    return side_env
        

def scanEnvironment(matrix, row, column):
    top_env = scanTopEnvironment(matrix, row, column)
    bottom_env = scanBottomEnvironment(matrix,row,column)
    side_env= scanSideEnvironment(matrix,row,column)
    
    environment = top_env + bottom_env + side_env
            
    return environment





# Open data
matrix = []

with open('Day 3\data.txt', 'r') as f:
    for line in f.read().split('\n'): 
        newline = list(line)
        matrix.append(newline)




####### PART 1





part_numbers = []

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        current_char = matrix[i][j]
        
        prev_env = []
        prev_prev_env = []
        
        if isNumber(current_char):
            
            number = int(current_char)
            
            env = scanEnvironment(matrix,i,j)
            
            prev_char = scanSideEnvironment(matrix,i,j)[0]
            
            if isNumber(prev_char):
                number = int(prev_char + current_char)
                
                prev_env = scanEnvironment(matrix,i,j-1)
                
                prev_prev_char = scanSideEnvironment(matrix,i,j-1)[0]
                
                if isNumber(prev_prev_char):
                    number = int(prev_prev_char+prev_char+current_char)
                    
                    prev_prev_env = scanEnvironment(matrix,i,j-2)
                
            env += prev_env + prev_prev_env
            env = set(env)
            
            next_char = scanSideEnvironment(matrix,i,j)[-1]
             
            if containsSymbol(env) and isNumber(next_char) == False:
                part_numbers.append(number)

            
answer1 = sum(part_numbers)
print('answer 1 =', answer1)
        




########### PART 2






# Dumb creation of matrix where all digits are replaced by full-lenght int digits. E.g. ['a', '1', '2', '3', 'b' ]
# becomes ['a', 123, 123, 123, 'b' ]....

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        current_char = matrix[i][j]
        number = ''

        if isNumber(current_char):
            
            number = current_char
            prev_char = scanSideEnvironment(matrix,i,j)[0]
            
            x_digits = 0
            
            if isNumber(prev_char):
                number = prev_char + current_char
                prev_prev_char = scanSideEnvironment(matrix,i,j-1)[0]
                
                x_digits += 1
                
                if isNumber(prev_prev_char):
                    number = prev_prev_char+prev_char+current_char
                    
                    x_digits +=1
        
        next_char = scanSideEnvironment(matrix,i,j)[-1]
        
        if number != '' and isNumber(next_char) == False:
            for x in range(0,x_digits+1):
                matrix[i][j-x] = int(number)
                
    
                


# Check if char = asterisk and if its environment contains two numbers. 
# Get ratio if that's the case.

ratios = []

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        current_char = matrix[i][j]
        if isStar(current_char):
            env = scanEnvironment(matrix,i,j)

            env = [char for char in env if type(char) == int]
            
            env = np.unique(env)
            
            if len(env) == 2:
                ratio = env[0] * env[1]
                ratios.append(ratio)


answer2 = sum(ratios)
print('answer 2 =', answer2)
                
            
