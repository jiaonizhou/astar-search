import environment
import state

class Search: 
	def __init__(self, initial_state, env):
		self.initial_state = initial_state
		self.env = env

	def search(self):
		frontier = [self.initial_state]
		frontier_all = [(self.initial_state.x_pos, self.initial_state.y_pos)]
		visited = []
		while frontier:
			candidate = frontier.pop()
			visited.append(candidate)
			# print candidate

			if candidate.cost_so_far <= 100 and self.env.is_goal(candidate):
				solution = candidate
				return (solution, frontier, visited)
			elif candidate.cost_so_far > 100:
				continue
			else:
				pos_n = candidate.y_pos + 1
				pos_e = candidate.x_pos + 1
				pos_s = candidate.y_pos - 1
				pos_w = candidate.x_pos - 1
				child_n = None
				child_e = None
				child_s = None
				child_w = None
				if pos_n <= self.env.end_y:
					child_n = state.State(candidate.x_pos, pos_n)
					child_n.astar = self.env.calc_astar(candidate, child_n)[1]
					child_n.cost_so_far = self.env.calc_astar(candidate, child_n)[0]
					child_n.moves_so_far = candidate.moves_so_far + ['N']
				if pos_e <= self.env.end_x:
					child_e = state.State(pos_e, candidate.y_pos)
					child_e.astar = self.env.calc_astar(candidate, child_e)[1]
					child_e.cost_so_far = self.env.calc_astar(candidate, child_e)[0]
					child_e.moves_so_far = candidate.moves_so_far + ['E']
				if pos_s >= 0:
					child_s = state.State(candidate.x_pos, pos_s)
					child_s.astar = self.env.calc_astar(candidate, child_s)[1]
					child_s.cost_so_far = self.env.calc_astar(candidate, child_s)[0]
					child_s.moves_so_far = candidate.moves_so_far + ['S']
				if pos_w >= 0:
					child_w = state.State(pos_w, candidate.y_pos)
					child_w.astar = self.env.calc_astar(candidate, child_w)[1]
					child_w.cost_so_far = self.env.calc_astar(candidate, child_w)[0]
					child_w.moves_so_far = candidate.moves_so_far + ['W']

				l = [child for child in [child_w, child_s, child_e, child_n] if child is not None and (child.x_pos, child.y_pos) not in frontier_all]
				l.sort(key=lambda x: x.astar, reverse=True)
				for child in l:
					frontier.append(child)
					frontier_all.append((child.x_pos, child.y_pos))
		return None

