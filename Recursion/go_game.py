#Q: Play Go on a grid. Black stones and white stone. 
# Dead - white stone with a stone above, below, left, right 
# color matters. 
# All of contiguous stones are either all dead or alive
# Goal: a fnc that takes ina board, x, and y coord and based on that return t/F

# Case 
# 1: if any important space is empty then not dead
# 2: check for all 4 stones of opposite color or contiguous array of stones of same color

import numpy


class Go(object):
	def __init__(self, board_size):
		self.board_size = board_size
		self.board = numpy.zeros((board_size, board_size))
		self.player1 = 1
		self.player2 = 2

	def check_space_death(self, x_coord, y_coord):
		coords = [(x_coord-1, y_coord), (x_coord-1+1, y_coord), (x_coord, y_coord-1), (x_coord, y_coord+1)]
		neighbors = list()
		for x,y in coords:
			neighbors.append(((x,y), board[x][y]))
			if self.board[x][y] == 0:
				return (False, 0)
		return (True, neighbors) 

	def is_dead(self, x_coord, y_coord, other_player_value, spaces_checked = dict()):
		if (x_coord, y_coord) in spaces_checked.keys():
			return spaces_check[(x_coord, y_coord)]

		is_empty, neighbors = self.check_space_death(x_coord, y_coord)
		#check impr spaces for empty space -> alive
		if not is_empty:
			spaces_checked[(x_coord, y_coord)] = False
			return False 
		else:
			#check for all other player -> dead
			neighbor_values = set([tup[-1] for tup in neighbors])
			if len(neighbor_values) == 1 and neighbor_values[0] == other_player_value:
				spaces_checked[(x_coord, y_coord)] = True
				return True
			#check for all other player, except for contiguous same player -> recursive
			end_result = list()
			for x,y, player_value in neighbors:
				if player_value != other_player_value:
					#return 
					end_result.append(self.is_dead(x, y, other_player_value, spaces_checked))
			return all(end_result)
	
			



		
		
		
		#(keep track of places we already visited )

