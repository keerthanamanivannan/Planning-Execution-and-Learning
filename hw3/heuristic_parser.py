#!/usr/bin/env python
def heuristic(filename):
	#filename = 'heuristic_1.txt'
	with open(filename) as f:
		data = f.readlines()

	f = open(filename)
	data = f.readlines()
	f.close()

	l = []
	H = []
	for n, line in enumerate(data, 1):
		l.append(line.rstrip())

	for i in range(len(l)):	
		H.append(l[i].split(","))
		H[i] = map(int, H[i])
	return H
