'''
Problem:
You must find the 1st, 2nd and 3rd fastest horses. But you only know the ranking of each race and can only make races in groups of 5 horses.


My solution...

'''

import random


# Create random 25 horses in a list
horses = []                             # create an empty list of horses
for i in range (0,25):                  # assign a random value to x, between 1 and 100, which will be the speed
    x = random.randrange(+10, 100)
    horses.append(x)


# Divide in 5 groups
group = [horses[0:5],horses[5:10],horses[10:15],horses[15:20],horses[20:25]]


# Print the horses list for further comparisons
print('Here are the horses:')
for i in range (0, len(horses)):
    print('Horse',i + 1, ':',horses[i])


# Make the first 5 races. By sorting in reverse each best horse is the firt item of each list
group[0] = sorted(group[0], reverse= True)
group[1] = sorted(group[1], reverse= True)
group[2] = sorted(group[2], reverse= True)
group[3] = sorted(group[3], reverse= True)
group[4] = sorted(group[4], reverse= True)


# Make the 6th race
# The first item is the fastest horse of all the horses
group = sorted(group, reverse= True)


# Find the winner's position and add 1 for visualisation
winner_pos = [i for i,x in enumerate(horses) if x == group[0][0]]       # string search
winner_pos = [i + 1 for i in winner_pos]                                # add 1 so that the winner's position is not 0


# Print the winner(s)
length_winner_post = len(winner_pos)                                    # we need the length In case there is a draw
print('\nThe fastest horse is at position:',winner_pos[0:length_winner_post],'and had a speed of:', group[0][0])


# Make the last race
# Here is the tricky part : we mix up some horses depending how close they could be logically
last_race = group[0][1],group[0][2],group[1][0],group[1][1],group[2][0]
last_race_results = sorted(last_race, reverse=True)                     # we sort this race to have the 2nd and 3rd best horses


# Find the position of the winners and add 1 for visualisation
winner_pos2 = [i for i,x in enumerate(horses) if x == last_race_results[0]]
winner_pos3 = [i for i,x in enumerate(horses) if x == last_race_results[1]]
winner_pos2 = [i + 1 for i in winner_pos2]
winner_pos3 = [i + 1 for i in winner_pos3]


# Print the results of the last race
print('The second fastest horse is at position:',winner_pos2, 'and had a speed of:',last_race_results[0])
print('The third fastest horse is at position:',winner_pos3, 'and had a speed of:',last_race_results[1])

