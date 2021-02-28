import math


def eulerphi(n):
	count = 0
	for i in range(n):
		if math.gcd(n, i) == 1:
			count += 1
	return count
