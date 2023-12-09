total = []

with open('Day 4\data.txt', 'r') as f:
    for line in f.read().split('\n'):
        card_no = line.split(':')[0]
        card = line.split(':')[1]
         
        winning_nos = card.split('|')[0]
        scratched_nos = card.split('|')[1]
        
        winning_nos = winning_nos.split(' ')
        scratched_nos = scratched_nos.split(' ')
        
        winning_nos = [num for num in winning_nos if num != '']
        scratched_nos = [num for num in scratched_nos if num != '']
        
        total.append((winning_nos, scratched_nos))


total_wins = []

for card in total:
    wins = 0
    for winning_number in card[0]:
        if winning_number in card[1]:
            wins += 1
    
    if wins > 0:
        total_wins.append(1 * 2**(wins-1))


answer = sum(total_wins)
print('answer =', answer)

