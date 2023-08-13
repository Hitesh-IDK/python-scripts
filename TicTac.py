#Getting the rows ready
row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']

rows = {
    'A': row1,
    'B': row2,
    'C': row3
}

#Getting the combinations ready for the game
combinations = list(map(lambda cell: cell+'1 '+ cell+'2 ' + cell+'3' , ['A', 'B', 'C']))
possibleCombinations = []
for items in combinations:
    for item in items.split():
        possibleCombinations.append(item)
print(possibleCombinations)

#Display Function to display the rows
def display(rows):
    spliter = '_'*17
    print()
    print('   1     2     3')
    print(f'A  {rows["A"][0]}  |  {rows["A"][1]}  |  {rows["A"][2]}')
    print(spliter + '\n')
    print(f'B  {rows["B"][0]}  |  {rows["B"][1]}  |  {rows["B"][2]}')
    print(spliter+ '\n')
    print(f'C  {rows["C"][0]}  |  {rows["C"][1]}  |  {rows["C"][2]}')
    print()

#Validate and update the rows if the user input is correct
def validateInput(choice, player):
    if choice in possibleCombinations:
        possibleCombinations.remove(choice)
        row = choice[0]
        column = int(choice[1]) - 1
        if player == 1:
            rows[row][column] = 'X'
        else:
            rows[row][column] = 'O'
    else:
        print('Something went wrong~~!')

#Take in user input and continue to validate it
def takeUserInput(player):
    while True:
        userinput = input('Enter a cell number: ')
        if userinput.upper() not in possibleCombinations:
            print('Invalid Cell - Combinations allowed -> ', possibleCombinations)
        else:
            validateInput(userinput.upper(), player)
            break

#Game end logic, to check who wins
def gameEnd(rows):
    for row in rows.values():
        if row == ['X', 'X', 'X'] or row == ['O', 'O', 'O']:
            return True
        
    if rows['A'][0] == rows['B'][1] == rows['C'][2]:
        if rows['A'][0] == 'X' or rows['A'][0] =='O':
            return True
        
    if rows['A'][2] == rows['B'][1] == rows['C'][0]:
        if rows['A'][2] == 'X' or rows['A'][2] == 'O':
            return True
        
    if rows['A'][0] == rows['B'][0] == rows['C'][0]:
        if rows['A'][0] == 'X' or rows['A'][0] == 'O':
            return True
        
    if rows['A'][1] == rows['B'][1] == rows['C'][1]:
        if rows['A'][1] == 'X' or rows['A'][1] == 'O':
            return True
        
    if rows['A'][2] == rows['B'][2] == rows['C'][2]:
        if rows['A'][2] == 'X' or rows['A'][2] == 'O':
            return True
        
    return False

#Proper order of when to call the functions
import os
def gameStart():
    os.system('cls')
    display(rows)
    
    while True:
        print("Player 1's turn")
        takeUserInput(1)
        os.system('cls')
        display(rows)
        if gameEnd(rows):
            print("Player 1 Wins!")
            return;
        
        print("Player 2's turn")
        takeUserInput(2)
        os.system('cls')
        display(rows)
        if gameEnd(rows):
            print("Player 2 Wins!")
            return;

if __name__ == '__main__':
    gameStart()