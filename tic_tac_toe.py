import random

### reset game board to empty
def reset_Whiteboard(my_List):
    my_List = [ [] ] * 3
    my_List[0] = [" ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " ", "\n"]
    my_List[1] = [" ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " ", "\n"]
    my_List[2]= [" ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " ", "\n"]
    return my_List

### display the location user can choose in game board
def initial_Whiteboard(my_List):
    my_List = [ [] ] * 3
    my_List[0] = [" ", "7", " ", "|", " ", "8", " ", "|", " ", "9", " ", "\n"]
    my_List[1] = [" ", "4", " ", "|", " ", "5", " ", "|", " ", "6", " ", "\n"]
    my_List[2] = [" ", "1", " ", "|", " ", "2", " ", "|", " ", "3", " ", "\n"]
    return my_List

### transfer user input location to nested list column
def num_Transfer(num):
    if num in [1,4,7]:
        return 1
    if num in [2,5,8]:
        return 5
    else:
        return 9

### transfer user input location to nested list row
def list_Transfer(num):
    if num <= 3:
        return 2
    if num <=6 and num > 3:
        return 1
    else:
        return 0

### print updated game board so that user knows where the game at
def print_Update_Whiteboard(my_List):
    mystring1 = "   |   |   \n"
    mystring2 = "___|___|___\n"
    print(mystring1 + "".join(my_List[0]) + mystring2 + mystring1 + "".join(my_List[1]) + mystring2 + mystring1 + "".join(my_List[2]) +mystring1)

### according to user input to change the nested list element value which will gets reflected to game board
def change_Whiteboard(num, value, my_List):
    my_List[list_Transfer(num)][num_Transfer(num)] = value
    return my_List

### check if we have a winner when the game proceed
def check_Winner(value, my_List):
    if my_List[0][1] == my_List[1][5] == my_List[2][9] == value:
        return value
    if my_List[2][1] == my_List[1][5] == my_List[0][9] == value:
        return value
    count = 0
    for i in range(0,3):
        if my_List[i][1] == value:
            count += 1
        if count == 3:
            return value
    count = 0
    for i in range(0,3):
        if my_List[i][5] == value:
            count += 1
        if count == 3:
            return value
    count = 0
    for i in range(0,3):
        if my_List[i][9] == value:
            count += 1
        if count == 3:
            return value
    count = 0
    for j in [1, 5, 9]:
        if my_List[0][j] == value:
            count += 1
        if count == 3:
            return value
    count = 0
    for j in [1, 5, 9]:
        if my_List[1][j] == value:
            count += 1
        if count == 3:
            return value
    count = 0
    for j in [1, 5, 9]:
        if my_List[2][j] == value:
            count += 1
        if count == 3:
            return value          
    return ('None')

### check if it is a tie game
def even_Check(my_List):
    count = 0
    for i in range (0,3):
        for j in [1, 5, 9]:
            if my_List[i][j] != " ":
                count += 1
    if count == 9:
        print("No more position to fill, 2 players are even, please start the next game!")
        return True
    else:
        return False

### determine the winner which will be used in the main function
def determine_Winner(value, my_List):
    if check_Winner(value, my_List) == value:
        print ("Player who plays {} is the WINNER!!!".format(value))
        return True
    else:
        return False

### validate user input for characters
def check_Value(x):
    
    value = 'invalid'
    
    valid_Value = False
    
    while valid_Value == False:
        value = input("Please choose a value represent your player(choose from 'x' or 'o' only): ")
        if value not in ('x','o'):
            print("Invalid position, you should choose from either 'x' or 'o' please!")
        elif value == x:
            print("Other player already choosed {}, please choose the other one.".format(value))
        else:
            valid_Value = True
    
    return value

### double check with the user whether she or he wants to continue/replay the game
def game_Continue():
    
    game = 'invalid'
    
    valid_Choice = False
    while valid_Choice == False:
        game = input("Do you want to continue play/play again? (choose from 'Y' or 'N'): ")
        if game not in ('Y', 'N'):
            print("Invalid choice, please choose from 'Y' or 'N' only! ")
        else:
            valid_Choice = True
    
    return game

### generate a random number which represent which user will go first
def choose_first():
    
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

### main function for this tic tac toe game
def tic_Tac_Toe():
    # Initial part
    print ("Welcome to the game: TIC TAC TOE !!!")
    print ("Here is the game board you gonna play: ")
    my_List = [ [] ] * 3
    my_List = initial_Whiteboard(my_List)
    print_Update_Whiteboard(my_List)
    # Rule description:
    print ("This is a 2 player game, players gets to control to place 'x' or 'o' on board and whoever gets the first 3 'x' or 'o' continuesly inline gets to win!")
    print ("Now let's start the game!")
    while True:
        my_List = reset_Whiteboard(my_List)
        print ("Initial board looks like: ")
        print_Update_Whiteboard(my_List)
        # Ask user which character he/she wants to control
        turn = choose_first()
        print (turn + " will go first")
        
        value_x = ''
        
        if turn == 'Player 1':
            # Player1
            print ("Player1 please choose your charcter you want to use: ")
            player1_Value = check_Value(value_x)
            value_x = player1_Value
            # Player2
            print ("Player2 please choose your charcter you want to use: ")
            player2_Value = check_Value(value_x)
            
        
        if turn == 'Player 2':
            # Player1
            print ("Player2 please choose your charcter you want to use: ")
            player2_Value = check_Value(value_x)
            value_x = player2_Value
            # Player2
            print ("Player1 please choose your charcter you want to use: ")
            player1_Value = check_Value(value_x)
        
        
        # Game start
        print ("GAME START!!!")
        winner_Result = False
        even_Result = False
        position = []
        while winner_Result == False and even_Result == False:
            
            
            if turn == 'Player 1':
                # Player 1
                print ("Player1 it is your turn to choose a position: ")
                player1_Position = check_Position(position)
                position.append(player1_Position)
                my_List = change_Whiteboard(player1_Position, player1_Value, my_List)
                print_Update_Whiteboard(my_List)
                winner_Result = determine_Winner(player1_Value, my_List)
                if winner_Result == True:
                    break
                even_Result = even_Check(my_List)
                if even_Result == True:
                    break
                turn = 'Player 2'
            
            
            if turn == 'Player 2':
                # Player 2
                print ("Player2 it is your turn to choose a position: ")
                player2_Position = check_Position(position)
                position.append(player2_Position)
                my_List = change_Whiteboard(player2_Position, player2_Value, my_List)
                print_Update_Whiteboard(my_List)
                winner_Result = determine_Winner(player2_Value, my_List)
                if winner_Result == True:
                    break
                even_Result = even_Check(my_List)
                if even_Result == True:
                    break
                turn = 'Player 1'
        
        
        if game_Continue() == 'N':
            break
        else:
            pass
