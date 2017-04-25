import environment
import state

class Search: 
	def __init__(self, initial_state, env):
		self.initial_state = initial_state
		self.env = env

	def search(self):
		frontier = [self.initial_state]
		visited = []
		visited_pos = []
		while frontier:		
			frontier.sort(key=lambda x: x.astar)
			candidate = frontier.pop(0)
			visited.append(candidate)
			visited_pos.append((candidate.x_pos, candidate.y_pos))

			if self.env.is_goal(candidate):
				solution = candidate
				if frontier:
					frontier.reverse()
				return (solution, frontier, visited)
			else:
				pos_n = candidate.y_pos + 1
				pos_e = candidate.x_pos + 1
				pos_s = candidate.y_pos - 1
				pos_w = candidate.x_pos - 1
				child_n = None
				child_e = None
				child_s = None
				child_w = None
				new_child = []
				if pos_n <= self.env.height - 1:
					child_n = state.State(candidate.x_pos, pos_n)
					child_n.astar = self.env.calc_astar(candidate, child_n)[1]
					child_n.cost_so_far = self.env.calc_astar(candidate, child_n)[0]
					child_n.moves_so_far = candidate.moves_so_far + ['N']
					for s in frontier:
						if s.x_pos == child_n.x_pos and s.y_pos == child_n.y_pos:
							if child_n.astar >= s.astar:
								child_n = None
								break
							else:
								frontier.remove(s)
								break
				if pos_e <= self.env.width - 1:
					child_e = state.State(pos_e, candidate.y_pos)
					child_e.astar = self.env.calc_astar(candidate, child_e)[1]
					child_e.cost_so_far = self.env.calc_astar(candidate, child_e)[0]
					child_e.moves_so_far = candidate.moves_so_far + ['E']
					for s in frontier:
						if s.x_pos == child_e.x_pos and s.y_pos == child_e.y_pos:
							if child_e.astar >= s.astar:
								child_e = None
								break
							else:
								frontier.remove(s)
								break
				if pos_s >= 0:
					child_s = state.State(candidate.x_pos, pos_s)
					child_s.astar = self.env.calc_astar(candidate, child_s)[1]
					child_s.cost_so_far = self.env.calc_astar(candidate, child_s)[0]
					child_s.moves_so_far = candidate.moves_so_far + ['S']
					for s in frontier:
						if s.x_pos == child_s.x_pos and s.y_pos == child_s.y_pos:
							if child_s.astar >= s.astar:
								child_s = None
								break
							else:
								frontier.remove(s)
								break
				if pos_w >= 0:
					child_w = state.State(pos_w, candidate.y_pos)
					child_w.astar = self.env.calc_astar(candidate, child_w)[1]
					child_w.cost_so_far = self.env.calc_astar(candidate, child_w)[0]
					child_w.moves_so_far = candidate.moves_so_far + ['W']
					for s in frontier:
						if s.x_pos == child_w.x_pos and s.y_pos == child_w.y_pos:
							if child_w.astar >= s.astar:
								child_w = None
								break
							else:
								frontier.remove(s)
								break

				children = [child for child in [child_n, child_e, child_s, child_w] if child is not None and (child.x_pos, child.y_pos) not in visited_pos]
				for child in children:
					if child.cost_so_far <= self.env.energy_budget:
						frontier.append(child)
				
		solution = None

		return (solution, frontier, visited)

