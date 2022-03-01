import random
import sys

missions = []

# Input missions to choose from:
while True:
    print('Enter the name of a mission ' + str(len(missions) + 1) + ' (Or enter nothing to stop.):')
    mission = input()
    if mission == '':
        break
    missions = missions + [mission]    # list concatenation
print('The mission choices are:')
for mission in missions:
    print('  ' + mission) 

while True:     # The main loop
    while True:     # The main input loop
        print('Type (n)ext for next mission assignment or (q)uit to leave')
        choice = input()
        if str.casefold(choice) == 'q' :
            sys.exit()      # Quit the program
        if str.casefold(choice) == 'n':
            break   # Break out of input loop

    if str.casefold(choice) == 'n':
        print(missions[random.randint(0, len(missions) -1)])   # Display randomly selected mission    
    elif str.casefold(choice) != 'n':
        print('Please type n or q')

 
