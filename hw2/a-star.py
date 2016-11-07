#!/usr/bin/env python
import IPython
import sys
from parser import parser
from heuristic_parser import heuristic
import matplotlib.pyplot as plt
from PriorityQueue import PriorityQueue

def get_cost(C,state):
	(x,y,t) = state
	return C[x][y]

def get_heuristic(state1):
	(x1,y1,t1) = state1
	return weight*H[x1][y1]

def inBounds(state):
	(x,y,t) = state
	return 0<=x<N and 0<=y<N and t<len(pos)

def get_successors(state):
	(x,y,t) = state
	successors = [(x,y,t+1),(x+1,y,t+1),(x,y-1,t+1),(x-1,y,t+1),(x,y+1,t+1)]
	successors = filter(inBounds,successors)
	return successors

def reconstruct_path(plan,currentState):
	totalPath = [currentState]
	while(1):
		try:	
			currentState = plan[currentState]
			totalPath.append(currentState)
		except:
			break
	return totalPath

def visualize(path,C):
	plt.imshow(C)
	for i in range(len(path)):
		plt.scatter(x=path[i][1],y = path[i][0],c='b')
	plt.show()

def get_totalCost(plan,C):
	totalCost = 0
	for i in range(len(plan)):
		(x,y,t) = plan[i]
		totalCost = totalCost + C[x][y]
	print totalCost

def Astar(start,goal,C):
	openSet = PriorityQueue()
	openSet.put(start,0)
	openSet_check = {}
	openSet_check[start]=1
	closedSet = {}
	plan = {}
	g = {}
	g[start] = 0
	f = {}
	j=0
	f[start] = get_heuristic(start)
	p=0
	while not openSet.empty():
		currentState, fpop = openSet.get()
		if currentState in goal:
			path = reconstruct_path(plan,currentState)
			path.reverse()			
			get_totalCost(path,C)
			visualize(path,C)
			for i in range(len(path)):
				print path[i]
			break

		closedSet[currentState] = 1
		for nextState in get_successors(currentState):
			j=j+1
			if nextState in closedSet:
				continue

			newCost = g[currentState] + get_cost(C,nextState)
			if nextState not in openSet_check:
				plan[nextState] = currentState
				g[nextState] = newCost
				f[nextState] = g[(nextState)] + get_heuristic(nextState)

				openSet.put(nextState,f[nextState])
				openSet_check[nextState] = 1
				continue

			elif newCost >= g[nextState]:
				openSet_check[nextState] = 1
				continue
			
			plan[nextState] = currentState
			g[nextState] = newCost
			f[nextState] = g[(nextState)] + get_heuristic(nextState)

			openSet.put(nextState, f[nextState])
			openSet_check[nextState] = 1
	return False

def main():
	global N, H, C, pos, weight
	N,R,pos,C = parser(sys.argv[1])
	H = heuristic(sys.argv[2])
	weight = int(sys.argv[3])
	for i in range(len(H)):
		for j in range(len(H)):
			if H[i][j] - C[i][j] > 0:
				H[i][j] = H[i][j] - C[i][j]
			else:
				H[i][j] = 0

	R.append(0)
	goal = {}
	start = tuple(R)
	for i in range(len(pos)):
		pos[i].append(i)
		goal[tuple(pos[i])] = 1
	Astar(start,goal,C)

if __name__ == "__main__": 
	main()
