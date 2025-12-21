import math

def sigmoid(z: float) -> float:
	#Your code here
	sig = (1 / (1+ math.exp(-z)))
	return round(sig,4)