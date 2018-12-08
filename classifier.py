import numpy as np
from math import log

# binary data
# each row is a person
# the last number in the row is CMV class
# all other data is TCR's

# generate data with the following probabilities to have a given TCR
# the last one denotes class, thus 1.0 and 0.0
r_1 = np.array([0.6, 0.4, 0.1, 0.1, 0.7, 0.9, 0.3, 1.0])
r_0 = np.array([0.9, 0.8, 0.5, 0.4, 0.1, 0.05, 0.2, 0.0])

N = len(r_1)
M = 25

d1 = np.random.uniform(size = N*M).reshape(M, N) + r_1
d1 = np.floor(d1).astype(int)


d0 = np.random.uniform(size = N*M).reshape(M, N) + r_0
d0 = np.floor(d0).astype(int)

print(d1)
print(d0)

d = np.concatenate((d1, d0), axis=0)

#d = np.array([[1,1,0,1], [1,1,0,1], [0,1,0,0], [0,1,0,0],[0,1,0,0], [0,1,0,0],[0,1,1,1],[0,1,1,1],[0,1,1,1]])

print("data", d)

def classify(data, x):

	# get data with the class 1 (CMV+)
	a = data[:,-1]
	condition = (a==1)
	data_1 = data[condition][:, :-1]

	# number of people in class 1
	n_plus = len(data_1)
	# number of people in total
	n_total = len(data)
	# number of people in class 0 (CMV-)
	n_minus = n_total - n_plus


	# number of each TCR appearing in class 1
	i_1 = np.sum(data_1, axis=0)

	# calculate the simple Bayes probabilities
	probs_1 = ( i_1 + 1 ) / (n_plus + 2)


	# get data with the class 0 (CMV-)
	b = data[:,-1]
	condition = (b==0)
	data_0 = data[condition][:, :-1]

	i_0 = np.sum(data_0, axis=0)
	probs_0 = ( i_0 + 1 ) / (n_minus + 2)

	# calculate the probability that x happens

	# x = [1, 0, 0]
	# probs_1 = [0.4, 0.5, 0.7]
	# yields [0.4, 0.5, 0.3], for example

	probs_1 = np.abs( np.abs(probs_1 - x) - 1)

	probs_0 = np.abs( np.abs(probs_0 - x) - 1)


	# calculate the likelihoods
	p_a = np.prod(probs_1) * (n_plus + 1) / (n_plus + 2)
	print("p_a", p_a)
	p_b = np.prod(probs_0) * (n_minus + 1) / (n_minus + 2)
	print("p_a", p_b)

	# calculate class probabilities based on the likelihoods
	p_total = p_a / (p_a + p_b)

	# return more likely class and its respective probability 
	c = 1
	if p_b > p_a:
		c = 0
		p_total = 1 - p_total

	return c, p_total



def loo(M):
	logloss = 0.0
	corr = 0
	for i in range(len(M)):

		x = M[i, :]
		M_0 = M.copy()
		M_0 = np.delete(M_0, i, axis=0)
		#print(M)
		print(x)
		#print(M_0)

		c, p = classify(M_0, x[:-1])

		print(c, p)
		if c == x[-1]:
			print("correct class", c)
			corr += 1
			logloss += log(p)
		else:
			print("incorrect class", c)
			logloss += log(1 - p)

	print("Accuracy", corr / len(M))
	logloss = logloss / len(M)
	print("Log loss", logloss)

loo(d)
