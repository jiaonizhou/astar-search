import environment

class Search: 
	def __init__(self, initial_state, env):
		self.initial_state = initial_state
		self.env = env

	def search(self):
		frontier = [self.initial_state]
		visited = []
		while frontier:
			candidate = frontier.pop()
			
			visited.add(candidate)
			if (env.is_goal(candidate))
				solution = candidate
				return (solution, frontier, visited)
			else
				if (self.initial_state.y_pos++ <= env.end_y) 
					child_n = state.State(self.initial_state.x_pos, self.initial_state.y_pos++)
					astar_n = env.calc_astar(candidate, child_n)[1]
				if (self.initial_state.x_pos++ <= env.end_x)
					child_e = state.State(self.initial_state.x_pos++, self.initial_state.y_pos)
					astar_e = env.calc_astar(candidate, child_e)[1]
				if (self.initial_state.y_pos-- >= 0)
					child_s = state.State(self.initial_state.x_pos, self.initial_state.y_pos--)
					astar_s = env.calc_astar(candidate, child_s)[1]
				if (self.initial_state.x_pos-- >= 0)
					child_w = state.State(self.initial_state.x_pos--, self.initial_state.y_pos)
					astar_w = env.calc_astar(candidate, child_w)[1]
				frontier.add(child_n)
				frontier.add(child_e)
				frontier.add(child_s)
				frontier.add(child_w)
		return None
