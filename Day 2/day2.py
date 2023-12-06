import pandas as pd
import numpy as np

# Open data
with open('Day 2\data.txt', 'r') as f:
    lines = f.read().split('\n')
f.close()


############ PART 1

data = {}
colors = ['red', 'green', 'blue']

total = sum(list(range(1,101)))

# create outer dictionary (game:draws)
for line in lines:

    key = line.split(':')[0]
    value = line.split(':')[1]

    new_key = key.split(' ')[1]
    int_key = int(new_key)

    data[int_key] = value
    

# create inner dictionary (draw:amount per color)
for key,value in data.items():

    game_dict = {}
    game_list = value.split(';')
    index = 1

    for draw in game_list:

        draw_dict = {}

        for color in colors:
                  
            if color in draw:
                try:
                    amount = int(draw[draw.index(color)-3:draw.index(color)-1])
                except:
                    amount = int(draw[draw.index(color)-2])
                draw_dict[color] = amount
            else:
                draw_dict[color] = 0
    
        game_dict[index] = draw_dict
        index += 1
    
    data[key] = game_dict


# transform data into multi-index dataframe
reformed_dict = {}

for outerKey, innerDict in data.items(): 
    for innerKey, values in innerDict.items(): 
        reformed_dict[(outerKey, 
                       innerKey)] = values 

df = pd.DataFrame(reformed_dict) 
df = df.transpose()
#print(df.to_markdown())

# filter impossible games
impossible = df[(df['red'] > 12) | (df['green'] > 13) | (df['blue'] > 14)]


# add impossible game ids to list 
impossible_list = []
impossible_game_ids = impossible.index


for i in impossible_game_ids:
    if i[0] not in impossible_list:
        impossible_list.append(i[0])


# subtract sum of impossible game ids from total sum of game ids
total_impossible = sum(impossible_list)
answer = total - total_impossible

print(answer)

############ PART 2


total2 = []

for i in range(1,101):
    min_red = df.loc[[i]]['red'].max()
    min_green = df.loc[[i]]['green'].max()
    min_blue = df.loc[[i]]['blue'].max()
    
    total2.append(min_red * min_green * min_blue)

answer2 = sum(total2)
print(answer2)
