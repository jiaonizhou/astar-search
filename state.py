class State:

	def __init__(self, x_pos, y_pos):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.moves_so_far = []
		self.cost_so_far = 0

	def _str_(self):
		state = 'Pos=(' + self.x_pos + ', ' + self.y_pos + ') Moves=['
		for move in self.moves_so_far :
			state += "'" + move + "', "
		state += self.moves_so_far 
		state += '] Cost=' + self.cost_so_far
		return state
