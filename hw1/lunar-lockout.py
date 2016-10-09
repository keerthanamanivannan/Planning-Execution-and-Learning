#!/usr/bin/env python
from bfs import bfs

#Initializing Initial States
#O-Orange; G-Green; P-Purple; Y-Yellow; B-Blue
level_9 = {"X": (0,2), "O": (0,4), "G": (2,2), "P": (3,1), "Y": (4,3)}
level_18 = {"X": (0,2), "O": (4,0), "G": (4,2), "P": (4,4)}
level_27 = {"X": (4,4), "O": (0,1), "G": (0,4), "P": (2,0), "B": (4,0), "Y": (2,3)}
level_36 = {"X": (0,2), "O": (1,0), "G": (1,4), "P": (3,0), "Y": (3,4), "B": (4,2)}

puzzle_levels = ["level 9"] + ["level 18"] + ["level 27"] + ["level 36"]
puzzles = [level_9, level_18, level_27, level_36]

num = 0

a = [9,18,27,36]
for i, val in enumerate(a):
  puzzle = puzzles[i]
  name = puzzle_levels[i]
  print("Solving Puzzle " + name)
  num+=bfs(puzzle, name)
  print "No. of states explored: ", num