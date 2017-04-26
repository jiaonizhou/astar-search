import environment
import state
import math

class Search:
	def __init__(self, initial_state, env):
		self.env = env
		self.start_state = initial_state
		self.end_state = state.State(self.env.end_x, self.env.end_y)

	def search(self):
		frontier_start = [self.start_state]
		frontier_end = [self.end_state]
		visited_start = []
		visited_end = []

		while frontier_start and frontier_end:

			cur_state_start = frontier_start.pop(0);
			cur_state_end = frontier_end.pop(0);

			visited_start.append(cur_state_start)
			visited_end.append(cur_state_end)

			meet = self.is_meet(cur_state_start, visited_end)
			if meet:
				solution = cur_state_start
				solution.moves_so_far += self.reversed_meet(meet)
				solution.cost_so_far += meet.cost_so_far
				frontier = frontier_start + frontier_end
				visited = visited_start + visited_end
				return (solution, frontier, visited)

			for move in self.env.availableMoves(cur_state_start):
				self.add_move(cur_state_start, move, frontier_start, visited_start)
			for move in self.env.availableMoves(cur_state_end):
				self.add_move(cur_state_end, move, frontier_end, visited_start)

		solution = []
		frontier = frontier_start + frontier_end
		visited = visited_start + visited_end
		return (solution, frontier, visited)

	def is_meet(self, cur_state, visited):
		for s in visited:
			if cur_state.x_pos == s.x_pos and cur_state.y_pos == s.y_pos:
				return s
		return None

	def reversed_meet(self, cur_state):
		cur_state.moves_so_far.reverse()
		reversed_move = []
		for move in cur_state.moves_so_far:
			if move == 'N':
				reversed_move.append('S')
			if move == 'S':
				reversed_move.append('N')
			if move == 'E':
				reversed_move.append('W')
			if move == 'W':
				reversed_move.append('E')
		return reversed_move

	def add_move(self, cur_state, move, frontier, visited):
		if move == 'N':
			next_move = state.State(cur_state.x_pos, cur_state.y_pos + 1)
			next_move.cost_so_far = cur_state.cost_so_far + self.moveCost(cur_state, next_move)
			next_move.moves_so_far = cur_state.moves_so_far + ['N']
			self.add_to_frontier(next_move, frontier, visited)
		elif move == 'E':
			next_move = state.State(cur_state.x_pos + 1, cur_state.y_pos)
			next_move.cost_so_far = cur_state.cost_so_far + self.moveCost(cur_state, next_move)
			next_move.moves_so_far = cur_state.moves_so_far + ['E']
			self.add_to_frontier(next_move, frontier, visited)
		elif move == 'S':
			next_move = state.State(cur_state.x_pos, cur_state.y_pos - 1)
			next_move.cost_so_far = cur_state.cost_so_far + self.moveCost(cur_state, next_move)
			next_move.moves_so_far = cur_state.moves_so_far + ['S']
			self.add_to_frontier(next_move, frontier, visited)
		elif move == 'W':
			next_move = state.State(cur_state.x_pos - 1, cur_state.y_pos)
			next_move.cost_so_far = cur_state.cost_so_far + self.moveCost(cur_state, next_move)
			next_move.moves_so_far = cur_state.moves_so_far + ['W']
			self.add_to_frontier(next_move, frontier, visited)

	def moveCost(self, cur_state, nextMove):
		diff = self.env.elevations[nextMove.y_pos][nextMove.x_pos] -  self.env.elevations[cur_state.y_pos][cur_state.x_pos]
		if diff > 0:
			cost = 1 + math.pow(diff, 2)
		elif diff < 0:
			cost = 1 + abs(diff)
		else:
			cost = 1
		return cost

	def add_to_frontier(self, cur_state, frontier, visited):
		if cur_state.cost_so_far > self.env.energy_budget:
			return
		if any(cur_state.x_pos == s.x_pos and cur_state.y_pos == s.y_pos for s in visited):
			return
		for s in frontier:
			if cur_state.x_pos == s.x_pos and cur_state.y_pos == s.y_pos:
				if cur_state.astar >= s.astar:
					return
				else:
					frontier.remove(s) 
		frontier.append(cur_state)



