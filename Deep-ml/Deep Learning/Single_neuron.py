import math
import numpy as np

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	# Your code here
    X = np.array(features , dtype = float)
    y = np.array(labels , dtype = float)
    w = np.array(weights , dtype = float)

    z = X @ w + bias
    probabilities = 1 / ( 1 + np.exp(-z))
    mse = np.mean((probabilities - y)**2) 

    return [round(p , 4) for p in probabilities], round(mse , 4)