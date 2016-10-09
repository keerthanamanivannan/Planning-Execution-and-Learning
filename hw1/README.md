#lunar-lockout-puzzle
CMU-15887 Homework1
Author: Keerthana Manivannan

The Initial States are given as input in the main lunar-lockout.py file.

Files:
1. bfs.py - Breadth First Search Planner
2. lunar-lockout.py - contains the Initial States and calls the bfs
3. State.py - a class which contains all the actions that happen in the problem;
	functions:get_path, get_moves, make_move, is_solved, get_valid_moves, get_previous

Running the program:
1. Run ./lunar-lockout.py in the terminal

Interpreting the results:
The program outputs each goal move in each round, where a move is of the form (bot, pos) 
e.g. ("X", (2,3)) means that the bot X has to be moved to the position (2,3) in the particular round