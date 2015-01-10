#Q: quickly check the winner for a tic tac toe game
#A: there are obvious combinations to check
import random 

#generate row, col combos

def generate_combos():
	combos = [((0,0), (1,1), (2,2)), ((0,2), (1,1), (2,0))]
	for i in range(3):
		combos.append([(i,y) for y in range(3)])
		combos.append([(y, i) for y in range(3)])
	return combos

def check_board(combos, board):
	for winning_check in combos:
		values = [board[y][x] for x,y in winning_check]
		if len(set(values)) == 1:
			return True, values[0]
	return False, None

def gen_board():
	return [[random.randint(0,2) for i in range(3)] for i in range(3)]

def main():
	board = gen_board()
	print(board)
	winning_combos = generate_combos()
	print(check_board(winning_combos, board))

main()