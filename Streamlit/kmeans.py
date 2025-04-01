import streamlit as st
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

def run_kmeans():
    st.title("K-Means Clustering")

    # Generate sample data
    X, y = make_blobs(n_samples=300, centers=3, random_state=42)

    # Get user input for number of clusters
    n_clusters = st.slider("Select Number of Clusters", 2, 10, 3)

    # Initialize and fit KMeans
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    y_pred = kmeans.fit_predict(X)

    # Plot the data
    fig, ax = plt.subplots()
    ax.scatter(X[:, 0], X[:, 1], c=y_pred, cmap='viridis', edgecolor='k')
    ax.set_title(f"K-Means Clustering (Clusters={n_clusters})")
    ax.set_xlabel("Feature 1")
    ax.set_ylabel("Feature 2")

    # Display plot
    st.pyplot(fig)
