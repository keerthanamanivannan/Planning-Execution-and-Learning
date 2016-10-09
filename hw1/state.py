#!/usr/bin/env python
import IPython
class State:

  def __init__(self, positions, n=0, previous=None, move=None):

    #Positions are Dictionary mapping strings ("A", "B", etc) to tuples (row,col)
    #e.g. {"A": (1,4), "B": (3,2), ...}
    self.positions = positions
    self.n = n 
    self.previous = previous
    self.move = move

  def get_previous(self):
    #Returns the previous State that got to the current state
    return self.previous

  def get_move(self):
    #Returns the move used to get to this State
    return self.move

  def get_path(self):
    #Returns: ([states], [moves])
    states = []
    moves = []
    cur_state = self
    cur_move = None
    while cur_state is not None:
      states.insert(0, cur_state)
      moves.insert(0, cur_state.get_move())
      cur_state = cur_state.get_previous()
    return (states, moves)

  def get_valid_moves(self):
    #Returns: list of moves, where a move is of the form (bot, pos) e.g. [("X", (0,1)),..]
    MOVES = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    occupied = set(self.positions.values())
    def can_move(bot, dir):
      if bot not in self.positions:
        return None
      (dr,dc) = MOVES[dir]
      (r_curr,c_curr) = self.positions[bot]
      #IPython.embed()

      # Make sure the new position is not blocked
      if (r_curr + dr, c_curr + dc) in occupied:
        return None

      #looping over to find possible moves
      #i intitialized to 2 because 1 doesn't make a difference
      for i in xrange(2, 5): 
        (r,c) = (r_curr + i*dr, c_curr + i*dc)
        #can't go overboard
        if r < 0 or r > 4 or c < 0 or c > 4:
          return None
        #if there is another bot in line of sight, it is a valid move
        if (r,c) in occupied:
          return (r-dr,c-dc)
      return None

    moves = []
    for bot in ('X', 'O', 'G', 'P', 'Y', 'B'):
      for dir in ('U', 'D', 'L', 'R'):
        move = can_move(bot, dir)
        if move:
          moves.append((bot, move))
    return moves

  def make_move(self,(bot, pos)):
    #Returns a new state where the bot has been moved in direction dir
    positions = {}
    for a, b in self.positions.iteritems():
      if bot == a:
        positions[a] = pos
      else:
        positions[a] = b
    return State(positions, n=self.n + 1, previous=self, move=(bot, pos))

  def is_solved(self):
    #Returns true if the game has been solved, i.e. when "X" is at position (2,2)
    return self.positions['X'] == (2,2)