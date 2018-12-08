import numpy as np


# binary data
# each row is a person
# the last number in the row is CMV class
# all other data is TCR's

data = np.array([[1,1,0,1], [0,1,0,0],[0,1,0,1]])

print("data", data)

def classify(x):


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
	print("probs", probs_1)


	# get data with the class 0 (CMV-)
	b = data[:,-1]
	condition = (b==0)
	data_0 = data[condition][:, :-1]

	i_0 = np.sum(data_0, axis=0)
	probs_0 = ( i_0 + 1 ) / (n_minus + 2)
	print("probs", probs_0)

	# calculate the probability that x happens

	# x = [1, 0, 0]
	# probs_1 = [0.4, 0.5, 0.7]
	# yields [0.4, 0.5, 0.3], for example

	probs_1 = np.abs( np.abs(probs_1 - x) - 1)
	print("probs1", probs_1)

	probs_0 = np.abs( np.abs(probs_0 - x) - 1)
	print("probs0", probs_0)


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



new = [1,0,1]

print(classify(new))