import numpy as np
def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
	# Your code here
	mse_values = []
	n = features.shape[0]
	updated_weights = initial_weights.copy()
	updated_bias = initial_bias
	
	for _ in range(epochs):
		#FeedForward
		z = (features @ updated_weights) + updated_bias
		probab = 1 / (1 + np.exp(-z))

		#Loss
		mse = np.mean((probab - labels)**2)
		mse_values.append(mse)
		
		#Backpropogation
		error = probab - labels
		dl_dz = 2 * (error) * ((probab)*(1 - (probab)))
		
		#Gradient
		dw = (features.T @ dl_dz)/n
		db = np.mean(dl_dz)
		
		#Weight Updates
		updated_weights -= learning_rate * dw
		updated_bias -= learning_rate * db

	r_weights = [round( w ,4) for w in updated_weights]
	r_bias = round(updated_bias,4) 

	return r_weights, r_bias, [round(m,4) for m in mse_values]