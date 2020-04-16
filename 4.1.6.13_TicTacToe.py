
theBoard = {'7': '7' , '8': '8' , '9': '9' ,
            '4': '4' , '5': '5' , '6': '6' ,
            '1': '1' , '2': '2' , '3': '3' }
board_keys = []
for key in theBoard:
    board_keys.append(key)

    
def DisplayBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])   
    

def EnterMove():
    global count
    count = 0
    global turn    
    turn = 'o'
    for i in range(10):
        print("\n")
        DisplayBoard(theBoard)
        move = input("\nIt's your turn, " + turn + " select a position on the board and press enter.\n")

        if theBoard[move] == move:
            theBoard[move] = turn
            ListFreeFields()
            count += 1
            print("\nOpen spaces: ", open_values)
            VictoryFor()
        else:
            print("That space is already take.\nMove to a new place.")
            
        if turn == 'o':
            turn = 'x'
        else:
            turn ='o'

  
def ListFreeFields():
    global open_values
    global random
    open_values = []
    for key, values in theBoard.items():
        if values not in ['o','x'] and key not in open_values:
            open_values.append(key)
#    random = open_values[0]

#def DrawMove():
 #   xturn = 'x'
  #  for i in open_values:
   #     if i in open_values:
    #        theBoard[random] = xturn
        
            

def VictoryFor():

    while count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
                DisplayBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                restart()
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
                DisplayBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                restart()
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
                DisplayBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                restart()
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
                DisplayBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                restart()
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
                DisplayBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                restart()            
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
                DisplayBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                restart()
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
                DisplayBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                restart()
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
                DisplayBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                restart()
            elif count == 9:
                print("\nGame Over\n")
                print("It's a tie")
                restart()
            else:
                return


def restart():
    restart = input("Do you want to play again? y or n?")
    if restart == "y":
        for key in board_keys:
            theBoard[key] = key
        EnterMove()
        resetCount
    elif restart == "n":

        exit()
    



EnterMove()
    
