import matplotlib.pyplot as plt
import numpy as np

y_list = []
with open("test.txt","r") as f:
	for line in f:
		y_list.append(line)

y = np.array((y_list),dtype=np.int32)
plt.plot(y)
plt.show()
