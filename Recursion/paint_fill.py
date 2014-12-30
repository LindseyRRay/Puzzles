#Q Code a paint fill finction that, given a screen, fills in screen with color
#until hits a pixel that is not of the original color

def screen_fill(coord_x, coord_y, orig_color, fill_color, screen):
	if screen[coord_y][coord_x] != orig_color or \
	screen[coord_x][coord_y] == fill_color :
		return False
	elif coord_x < 0 or coord_x > len(screen[0]) or \
	coord_y < 0 or coord_y > len(screen):
		return False
	else:
		screen[coord_y][coord_x] = fill_color
		screen_fill(coord.x-1, coord_y, color)
		screen_fill(coord.x+1, coord_y, color)
		screen_fill(coord.x, coord_y-1, color)
		screen_fill(coord.x, coord_y+1, color)

if __name__ == '__main__':
	# Create screen#
