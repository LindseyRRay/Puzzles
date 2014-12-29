#Q: a robot is sitting at upper left (0,0) of an X by Y grid. 
#They can only move right or down. How many possible paths from (0,0) to (X,Y)
import pdb
grid_x = 10
grid_y = 7

class Node:
	def __init__(self, value):
		self.position = value
		self.left = None
		self.right = None
		self.parent = None

def move_robot(current_position, possible_paths):
	if current_position[0] < 0 or current_position[1] < 0:
		return False
	else:
		if current_position == (0,0) or move_robot((current_position[0]-1, current_position[1]), possible_paths) \
		or move_robot((current_position[0], current_position[1]-1), possible_paths):
		#add current position to possible paths
			possible_paths.append(current_position)
			return True

def calculate_paths(current_position, root):
	if current_position == (10,7):
		return True, Node((10,7))
	else:
		if current_position == (0,0):
			current = root
		else:
			current = Node(current_position)
		left = (False, None)
		right = (False, None)
		if current_position[0] < grid_x:
			left = count_paths((current_position[0]+1, current_position[1]), current)
			if left[0]:
				current.left = left[1]
		if current_position[1] < grid_y:
			right = count_paths((current_position[0], current_position[1]+1), current)
			if right[0]:
				current.right = right[1]
		return (left[0] or right[0], current)

if __name__ == '__main__':
	paths = list()
	final = move_robot((10,7), paths)
	print(final)
	print(paths)

	head = Node((0,0))
	calculate_paths((0,0), head)
	