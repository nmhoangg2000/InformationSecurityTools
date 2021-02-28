import numpy as np


def cayley(n):
	table = np.zeros((n, n))
	for i in range(0, n):
		for j in range(0, n):
			table[i][j] = (i*j) % n
	return table
