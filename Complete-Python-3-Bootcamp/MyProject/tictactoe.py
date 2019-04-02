from IPython.display import clear_output
from random import randint
Player1 = ' '
Player2 = ' '
Playfirst = 0
board = ['#']+ [' ']*9
def display_board(board):
    print (board[1]+'|'+board[2]+'|'+board[3])
    print ("-----")
    print (board[4]+'|'+board[5]+'|'+board[6])
    print ("-----")
    print (board[7]+'|'+board[8]+'|'+board[9])


def player_input():
    global Player1
    global Player2
    Flag = True
    while True:
        Player1 = input("Player 1, which do you want, X or O?").upper()
        if Player1 == 'X':
            Player2 = 'O'
            break
        elif Player1 == 'O':
            Player2 = 'X'
            break
        else:
            print("Undefined Input")
    
    
    
def place_marker(board, marker, position):
    board[position]= marker
    return board

def win_check(board, mark):
	#print(board)
	#print(mark)
	ans = False
	ans = ans or (board[1]==board[2]==board[3]==mark)
	ans = ans or (board[4]==board[5]==board[6]==mark)
	ans = ans or (board[7]==board[8]==board[9]==mark)
	ans = ans or (board[1]==board[4]==board[7]==mark)
	ans = ans or (board[2]==board[5]==board[8]==mark)
	ans = ans or (board[3]==board[6]==board[9]==mark)
	ans = ans or (board[1]==board[5]==board[9]==mark)
	ans = ans or (board[3]==board[5]==board[7]==mark)
	return ans

def choose_first():
    return randint(1,2)

def space_check(board, position):
    return board[position]==' '

def full_board_check(board):
    return ' ' in board

def player_choice(board):
    while True:
        nextstep = input("Choose your next position (1-9)")
        if nextstep in "123456789":
        	nextstep = int(nextstep)
        	if space_check(board,nextstep):
        		return nextstep
        	else:
        		print("position {} is unavailable, please choose another position.".format(nextstep))
        else:
        	print("Wrong input")
def replay():
    while True:
        Ans = input("Do you want to replay? (Y-N)")
        if Ans=='Y':
            return True
        elif Ans == 'N':
            return False
        else:
            pass
def Init ():
	print("\n"*100)
	print("Player1 has choose: "+Player1)
	print("Player2 has choose: "+Player2)		
	print("Player {} play first".format(Playfirst))
	display_board(board)

print('Welcome to Tic Tac Toe!')

#while True:
#Set the game up here

while True:
	board = ['#']+[' ']*9
	print("\n"*100)
	player_input()
	Turn = choose_first()
	Playfirst = Turn
	while full_board_check(board):
		Init()
		if Turn == 1:
			print("Player1 turn")
			position = player_choice(board)
			if space_check(board,position):
				board = place_marker(board,Player1,position)
			Turn = 2
			if win_check(board,Player1):
				Init()
				print ("Player1 win")
				break
		else:
			print("Player2 turn")
			position = player_choice(board)
			if space_check(board,position):
				board = place_marker(board,Player2,position)
			Turn = 1
			if win_check(board,Player2):
				Init()
				print ("Player2 win")
				break
	else:
		Init()
		print("Draw")
	if not replay():
		break