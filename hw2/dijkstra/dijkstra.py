#!/usr/bin/env python
import IPython
import sys
from parser import parser
from PriorityQueue import PriorityQueue

def get_cost(C,state):
	(x,y) = state
	return C[x][y]

def inBounds(state):
	(x,y) = state
	return 0<=x<N and 0<=y<N

def get_successors(state):
	(x,y) = state
	successors = [(x+1,y),(x,y-1),(x-1,y),(x,y+1)]
	successors = filter(inBounds,successors)
	return successors

def dijkstra(start,C):
	openSet = PriorityQueue()
	openSet_check = {}

	closedSet = {}
	g = {}
	for i in range(len(start)):
		g[start[i]] = 0

	for i in range(len(start)):
		openSet.put(start[i],0)
		openSet_check[start[i]] = 1
	
	while not openSet.empty():
		currentState = openSet.get()
		closedSet[currentState] = 1
		for nextState in get_successors(currentState):
			if nextState in closedSet:
				continue

			newCost = g[currentState] + get_cost(C,nextState)
			if nextState not in openSet_check:
				g[nextState] = newCost
				openSet.put(nextState,g[nextState])
				openSet_check[nextState] = 1
			elif newCost >= g[nextState]:
				continue

			else:
				g[nextState] = newCost
				openSet.update(nextState,g[nextState])
				openSet_check[nextState] = 1
	
	temp = ''
	#For printing the H as a grid:
	'''for i in range(N):
		for j in range(N):
			if j==0:
				temp +=str(g[(i,j)])			
			else:
				temp +=','+str(g[(i,j)])
		temp += "\n"
	print temp'''
	
	#For writing the H onto a file
	f = open('heuristic.txt','w')
	temp=''
	for i in range(N):
		temp=''
		for j in range(N):
			if j==0:
				temp +=str(g[(i,j)])			
			else:
				temp +=','+str(g[(i,j)]) 
		if i==0:
			f.write(temp)
		else:
			f.write('\n'+temp)	
	f.close()
	return False

def main():
	start = []
	global N, C
	N,R,pos,C = parser(sys.argv[1])
	for i in range(len(pos)):
		start.append(tuple(pos[i]))
	dijkstra(start,C)

if __name__ == "__main__": 
	main()
