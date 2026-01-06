import math
import numpy as np

def softmax(scores: list[float]) -> list[float]:
	# Your code here
	scores = np.array( scores, dtype = float)
	exp_x = np.exp(scores)

	probabilities = exp_x / np.sum(exp_x)

	return [round(p, 4) for p  in probabilities ]

# EQUATION
# soft(x) = exp(x) / summation_till_j(exp(x_j))