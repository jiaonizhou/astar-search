#!/usr/bin/python

class State:

	def __init__(self, x_pos, y_pos):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.moves = ['n', 'v', 'e']
		self.cost = 0;

	def getState(self):
		output = "Pos = (" + str(self.x_pos) + ", " + str(self.y_pos) + ") Moves = " + str(self.moves) + " Cost = " + str(self.cost);
		return output

