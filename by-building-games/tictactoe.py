choices = []
for pos in range(0,9):
    choices.append(str(pos+1))
#creating Boolean variable
Is_Current_One = True #default player is player X
#first move is done by player X
won = False #at first we don't have any winner
while not won:
    print('\n')
    print('|' + choices[0] + '|' + choices[1] + '|' + choices[2] + '|')
    print('----------')
    print('|' + choices[3] + '|' + choices[4] + '|' + choices[5] + '|')
    print('----------')
    print('|' + choices[6] + '|' + choices[7] + '|' + choices[8] + '|')
    #above code is to print board layouts
    if Is_Current_One:        
        print("Player X")    
    else:        
        print("Player O")         
    try:
        choice = int(input("> ").strip())
    except ValueError:
        print("Please enter only valid fields from board (0-8)")
        continue  
    #code to put either X or O on position selected by user    
    if Is_Current_One:        
        try:
            choices[choice - 1] = 'X'
        except IndexError:
            print("Please enter only valid fields from board (0-8)")    
    else:        
        try:
            choices[choice - 1] = 'O'
        except IndexError:
            print("Please enter only valid fields from board (0-8)")    
    #code to toggle between True and False    
    Is_Current_One = not Is_Current_One
    
    #logic to make any player winner:
    for pos_x in range(0,3):
        pos_y = pos_x * 3 

        #for row condition:
        if (choices[pos_y] == choices[(pos_y + 1)]) and (choices[pos_y] 
            == choices[(pos_y + 2)]):
            #code to change won to True
            won = True #main loop will break
        
        #column condition:
        if (choices[pos_x] == choices[(pos_x + 3)]) and (choices[pos_x] 
            == choices[(pos_x + 6)]):
            won = True #main loop will break

        #diagonal condition here:
        if ((choices[0] == choices[4] and choices[0] == choices[8]) or
            (choices[2] == choices[4] and choices[4] == choices[6])):
            won = True

#print who is winner
print("Player " + str(int(Is_Current_One + 1)) + " won, Congratulations!")