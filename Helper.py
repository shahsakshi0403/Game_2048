def getChild(grid, dir):
	temp = grid.clone()
	temp.move(dir)
	return temp


def children(grid):
	children = []
	for move in grid.getAvailableMoves():
		children.append(getChild(grid, move))
	return children


def terminal(grid):
	return not grid.canMove()



def Eval(grid):
	import math 
	import numpy as np

	if terminal(grid):
		return -np.inf

	gradients = [
				[[ 3,  2,  1,  0],[ 2,  1,  0, -1],[ 1,  0, -1, -2],[ 0, -1, -2, -3]],   #Left
				[[ 0,  1,  2,  3],[-1,  0,  1,  2],[-2, -1,  0,  1],[-3, -2, -1, -0]],   #Right
				[[ 0, -1, -2, -3],[ 1,  0, -1, -2],[ 2,  1,  0, -1],[ 3,  2,  1,  0]],   #Up
				[[-3, -2, -1,  0],[-2, -1,  0,  1],[-1,  0,  1,  2],[ 0,  1,  2,  3]]    #Down
				]

	values = [0,0,0,0]

	for i in range(4):
		for x in range(4):
			for y in range(4):
				values[i] += gradients[i][x][y]*grid.map[x][y]

	
	return max(values)
