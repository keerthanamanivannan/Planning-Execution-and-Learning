#!/usr/bin/env python
from state import State
from collections import deque
import IPython

def bfs(start_dict, start_name):
  print("Running BFS")
  start_state = State(start_dict)
  visited = {}
  visited[start_state] = True
  q = deque([start_state])
  q.append(start_state)
  pop = 0

  while len(q) > 0:
    state = q.popleft()
    pop += 1
    if state.is_solved():
      states,moves = state.get_path()
      for i in xrange(len(moves)):
        print("Move " + str(i))
        print(moves[i])
      print "Total number of moves: " + str(len(moves))
      return pop
    
    moves = state.get_valid_moves()
    for move in moves:
      next_state = state.make_move(move)
      if next_state not in visited:
        q.append(next_state)
        visited[next_state] = True

  #Print if BFS doesn't find a solution
  print("BFS failed to find a solution") 
