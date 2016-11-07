import numpy
from copy import deepcopy

discountFactor = 0.8
prob = [[0.05, 0.05, 0.9], [0.25, 0.5, 0.25], [0.01, 0.02, 0.97]]
numActions = len(prob)

rewards = [1, -1, 0] # [None, Against, For]
initialPolicy = [1, 2, 0] # [Balanced = 0 , Offensive = 1, Defensive = 2]
Policy = deepcopy(initialPolicy)

stateValues = [0, 0, 0]

def updatePolicy(policy):
	currentPolicy = Policy
	for i in range(len(stateValues)):
		sum = 0
		for j in range(len(stateValues)):
			sum += prob[policy[i]][j]*stateValues[j]
		stateValues[i] = rewards[i] + discountFactor * sum
	vals = [0]*numActions
	for i in range(len(stateValues)):
		for j in range(numActions):
			sum = 0
			for k in range(len(stateValues)):
				sum += prob[j][k]*stateValues[k]
			vals[j] = rewards[i] + discountFactor*sum
		policy[i] =  vals.index(max(vals))
	return policy

while (True):	
	newPolicy = updatePolicy(Policy)
	if (newPolicy == Policy):
		break
	Policy = newPolicy

print "Discount Factor: " + str(discountFactor)
print "Initial Policy: " + str(initialPolicy)
print "Optimal Policy: "+ str(newPolicy)