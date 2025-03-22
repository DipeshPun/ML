from sklearn.cluster import KMeans
from sklearn import datasets
import matplotlib.pyplot as plt

# Generate sample data
X, y = datasets.make_blobs()

# Initialize KMeans with n_clusters=3
clf = KMeans(n_clusters=3)

# Fit the model to the data and predict the cluster labels
y_pred = clf.fit_predict(X)

# Plot the data points with colors according to predicted clusters
plt.figure(figsize=(10, 8))
plt.scatter(X[:, 0], X[:, 1], c=y_pred, cmap='viridis')
plt.title("K-Means Clustering Results")
plt.xlabel("X")
plt.ylabel("Y")

# Save the plot as an image
plt.savefig('kmeans_plot.png')  # Save plot to file
print("Plot has been saved as 'kmeans_plot.png'")
