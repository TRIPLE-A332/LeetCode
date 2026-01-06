import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	# Your code here
	X = np.array(scores , dtype = float)
	x = X - np.max(X)
	log_x = np.log(np.sum(np.exp(x)))
	probab = x - log_x

	return [round(p,4) for p in probab]


