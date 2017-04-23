#!/usr/bin/python

class Search:
	def __init__(self, initial_state, env):
		self.solution = [];
		self.frontier = [initial_state];
		self.visited = [initial_state];
		self.env = env;

