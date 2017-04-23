class State:

	def __init__(self, x_pos, y_pos):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.moves_so_far = []
		self.cost_so_far = 0
		self.astar = 0

	def __str__(self):
		state = 'Pos=(' + str(self.x_pos) + ', ' + str(self.y_pos) + ') Moves=['
		for move in self.moves_so_far:
			state += "'" + move + "', "
		state = state[:-2]
		state += '] Cost=' + str(self.cost_so_far)
		return state
