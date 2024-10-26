import matplotlib.pyplot as plt
from scipy.interpolate import Rbf
import seaborn as sns
import numpy as np

'''Random data points'''
heatmap_data = np.full((20, 40), -1)
# Select 20 random indices within the array to test how it displays stuff
indices = np.random.choice(range(20*40), size=20, replace=False)
# Assign random values between 0 and 10 to the selected indices
heatmap_data.flat[indices] = np.random.randint(0, 10, size=20)


'''interpolation'''
# Create a meshgrid for the indices
x, y = np.meshgrid(range(40), range(20))
hmp = np.copy(heatmap_data)
# Get the indices where the values are -1
unknown_indices = np.where(hmp == -1)
# Perform inverse distance weighted interpolation
rbf = Rbf(indices % 40, indices // 40, hmp.flat[indices])

# Assign the interpolated values to the unknown indices
hmp[unknown_indices] = rbf(unknown_indices[1], unknown_indices[0])

# Plot the heatmap using seaborn with the 'flare' colormap
hm = sns.heatmap(hmp, cmap='flare')
hm.set_aspect("equal")
# Plot the known points as transparent squares with black sides
known_points_x = indices % 40 + 0.5
known_points_y = indices // 40 + 0.5
plt.scatter(known_points_x, known_points_y, color='none', marker='s', edgecolor='black', linewidth=2, alpha=0.5)

# Show the plot
plt.show()