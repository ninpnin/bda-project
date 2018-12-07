import numpy as np

data = np.array([[1,1,0,1], [0,1,0,0],[0,1,0,1]])

print("data", data)

def classify(x):


	b = data[:,-1]
	condition = (b==1)
	data_1 = data[condition][:, :-1]

	print("data with class 1", data_1)

	n_plus = len(data_1)
	print(n_plus)

	n_total = len(data)
	n_minus = n_total - n_plus

	i_1 = np.sum(data_1, axis=0)

	print("i_1", i_1)

	probs_1 = ( i_1 + 1 ) / (n_plus + 2)

	print("probs", probs_1)


	b = data[:,-1]
	condition = (b==0)
	data_0 = data[condition][:, :-1]
	print("data_0", data_0)

	i_0 = np.sum(data_0, axis=0)
	print("i_0", i_0)
	probs_0 = ( i_0 + 1 ) / (n_minus + 2)
	print("probs", probs_0)

	print(x)
	probs_1 = np.abs( np.abs(probs_1 - x) - 1)
	print("probs1", probs_1)

	probs_0 = np.abs( np.abs(probs_0 - x) - 1)
	print("probs0", probs_0)

	p_a = np.prod(probs_1) * (n_plus + 1) / (n_plus + 2)
	print("p_a", p_a)
	p_b = np.prod(probs_0) * (n_minus + 1) / (n_minus + 2)

	print("p_a", p_b)

	p_total = p_a / (p_a + p_b)
	c = 1
	if p_b > p_a:
		c = 0
		p_total = 1 - p_total

	

	return c, p_total



new = [1,0,1]

print(classify(new))