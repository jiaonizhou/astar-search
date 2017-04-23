#!/usr/bin/python

import state
import sys

class Environment:
    'Map-based environment'

    # Member data
    # elevations: raw data for each position, stored in a list of lists
    #             (each outer list represents a single row)
    # height: number of rows
    # width: number of elements in each row
    # end_x, end_y: location of goal

    def __init__(self, mapfile, energy_budget, end_coords):
        self.elevations = []
        self.height = 0
        self.width = -1
        self.end_x, self.end_y = end_coords
        self.energy_budget = energy_budget
        # Read in the data
        for line in mapfile:
            nextline = [ int(x) for x in line.split() ]
            if self.width == -1:
                self.width = len(nextline)
            elif len(nextline) == 0:
                sys.stderr.write("No data (or parse error) on line %d\n"
                                 % (len(self.elevations) + 1))
                sys.exit(1)
            elif self.width != len(nextline):
                sys.stderr.write("Inconsistent map width in row %d\n"
                                 % (len(self.elevations) + 1))
                sys.stderr.write("Expected %d elements, saw %d\n"
                                 % (self.width, len(nextline)))
                sys.exit(1)
            self.elevations.insert(0, nextline)
        self.height = len(self.elevations)
        if self.end_x == -1:
            self.end_x = self.width - 1
        if self.end_y == -1:
            self.end_y = self.height - 1

    def is_goal(self, candidate):
        if (candidate.x_pos == self.end_x and candidate.y_pos == self.end_y) return True
        else return False

    def calc_astar(self, parent, child):
        if (self.elevations[child.y_pos][child.x_pos] > self.elevations[parent.y_pos][parent.x_pos]):
            cost = 1 + (self.elevations[child.y_pos][child.x_pos] - self.elevations[parent.y_pos][parent.x_pos]) ** 2
        elif (self.elevations[child.y_pos][child.x_pos] < self.elevations[parent.y_pos][parent.x_pos]):
            cost = 1 + (self.elevations[parent.y_pos][parent.x_pos] - self.elevations[child.y_pos][child.x_pos])
        else
            cost = 1
        heuristic = abs(self.end_x - child.x_pos) + abs(self.end_y - child.y_pos) + abs(self.elevations[end_y][end_x] - self.elevations[child.y_pos][child.x_pos])
        child.cost_so_far = parent.cost_so_far + cost
        astar = child.cost_so_far + heuristic
        return (child.cost_so_far, astar)



