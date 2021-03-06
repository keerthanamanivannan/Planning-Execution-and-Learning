import heapq
import IPython

class PriorityQueue:
	def __init__(self):
		self.elements=[]
	def empty(self):
		return len(self.elements)==0
	def put(self, state, priority):
		pair = (priority,state)
		heapq.heappush(self.elements,pair)
	def get(self):
		return heapq.heappop(self.elements)[1]
	def exists(self, state):
		return state in (x[1] for x in self.elements)
	def update(self,state,newF):
		for i,t in enumerate(self.elements):
			if t[1]==state:
				ind=i
				break
		#del self.elements[ind]
		self.get()
		self.put( state, newF)