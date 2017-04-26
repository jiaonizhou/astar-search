#!/usr/bin/python
import environment
import state
import math

class Search:
	def __init__(self, initial_state, env):
		self.solution = []
		self.frontier = [initial_state]
		self.visited = []
		self.env = env;
		

	def search(self):
		while self.frontier:
			# print "------frontier"
			self.frontier.sort(key=lambda x: x.astar)
			cur_state = self.frontier.pop(0);
			# print "------"
			# print "cur :(" + str(cur_state.x_pos) + ',' + str(cur_state.y_pos) + ") "
			# print self.env.availableMoves(cur_state)
			

			self.visited.append(cur_state);
			if self.env.isGoal(cur_state):
				self.solution = cur_state
				self.frontier.reverse()
				return (self.solution, self.frontier, self.visited)
			
			for move in self.env.availableMoves(cur_state):
				if move == 'N':
					next_move = state.State(cur_state.x_pos, cur_state.y_pos + 1)
					next_move.astar = self.moveCost(cur_state, next_move) + self.heuristic(next_move) + cur_state.cost_so_far
					next_move.cost_so_far = cur_state.cost_so_far + self.moveCost(cur_state, next_move)
					next_move.moves_so_far = cur_state.moves_so_far + ['N']
					self.add_to_frontier(next_move)
				elif move == 'E':
					next_move = state.State(cur_state.x_pos + 1, cur_state.y_pos)
					next_move.astar = self.moveCost(cur_state, next_move) + self.heuristic(next_move) + cur_state.cost_so_far
					next_move.cost_so_far = cur_state.cost_so_far + self.moveCost(cur_state, next_move)
					next_move.moves_so_far = cur_state.moves_so_far + ['E']
					self.add_to_frontier(next_move)
				elif move == 'S':
					next_move = state.State(cur_state.x_pos, cur_state.y_pos - 1)
					next_move.astar = self.moveCost(cur_state, next_move) + self.heuristic(next_move) + cur_state.cost_so_far
					next_move.cost_so_far = cur_state.cost_so_far + self.moveCost(cur_state, next_move)
					next_move.moves_so_far = cur_state.moves_so_far + ['S']
					self.add_to_frontier(next_move)
				elif move == 'W':
					next_move = state.State(cur_state.x_pos - 1, cur_state.y_pos)
					next_move.astar = self.moveCost(cur_state, next_move) + self.heuristic(next_move) + cur_state.cost_so_far
					next_move.cost_so_far = cur_state.cost_so_far + self.moveCost(cur_state, next_move)
					next_move.moves_so_far = cur_state.moves_so_far + ['W']
					self.add_to_frontier(next_move)
				# print str(move) + " astar: " + str(next_move.astar) + " cost: " + str(self.moveCost(cur_state, next_move)) + " manhattan: " + str(self.heuristic(next_move))

				
		return (self.solution, self.frontier, self.visited)

	def moveCost(self, cur_state, nextMove):
		# print "next: " + str(nextMove.y_pos) + ',' + str(nextMove.x_pos) + ", " + str(self.env.elevations[nextMove.y_pos][nextMove.x_pos])
		# print "cur: " + str(cur_state.y_pos) + ',' + str(cur_state.x_pos)
		diff = self.env.elevations[nextMove.y_pos][nextMove.x_pos] -  self.env.elevations[cur_state.y_pos][cur_state.x_pos]
		if diff > 0:
			cost = 1 + math.pow(diff, 2)
		elif diff < 0:
			cost = 1 + abs(diff)
		else:
			cost = 1
		# print "cost: " + str(cost)
		return cost

	def heuristic(self, cur_state):
		manhattan = abs(self.env.end_x - cur_state.x_pos) + abs(self.env.end_y - cur_state.y_pos) + abs(self.env.elevations[self.env.end_y][self.env.end_x] - self.env.elevations[cur_state.y_pos][cur_state.x_pos])
		# print "manhattan: " + str(manhattan)
		return manhattan


	def add_to_frontier(self, cur_state):
		if cur_state.cost_so_far > self.env.energy_budget:
			return
		if any(cur_state.x_pos == s.x_pos and cur_state.y_pos == s.y_pos for s in self.visited):
			return
		for s in self.frontier:
			if cur_state.x_pos == s.x_pos and cur_state.y_pos == s.y_pos:
				if cur_state.astar >= s.astar:
					return
				else:
					self.frontier.remove(s) 
		self.frontier.append(cur_state)
		



