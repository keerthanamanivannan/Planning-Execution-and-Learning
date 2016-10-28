#!/usr/bin/env python
def parser(filename):
	#filename = 'problem_1.txt'
	with open(filename) as f:
		data = f.readlines()
	f.close()

	l,T,B,C,pos = [],[],[],[],[]
	for n, line in enumerate(data, 1):
		l.append(line.rstrip())

	copyT, copyB = False, False
	for i in range(len(l)):
		if l[i] == 'N':
			N = l[i+1]
		if l[i] == 'R':
			R = l[i+1]

		#To strip T and store it as a list	
		if l[i] == 'T':
			copyT = True
		elif l[i] == 'B':
			copyT = False
		elif copyT:
			T.append(l[i])

		#To strip B and store it as a list	
		if l[i] == 'B':
			copyB = True
		elif i == len(l):
			copyB = False
		elif copyB:
			B.append(l[i])

	N = int(N)
	R = R.split(',')
	R = map(int, R)

	for i in range(len(T)):	
		pos.append(T[i].split(","))
		pos[i] = map(int, pos[i])

	#To break the string and store the cost and positions
	#as list of integer values
	for i in range(len(B)):	
		C.append(B[i].split(","))
		C[i] = map(int, C[i])

	return N,R,pos,C