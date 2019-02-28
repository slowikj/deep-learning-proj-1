import matplotlib.pyplot as plt
import numpy as np

def show_image(data_matrix, index):
	image=data_matrix[index,1:].reshape((28,28))
	plt.imshow(image)
	plt.show()
