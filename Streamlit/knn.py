import streamlit as st
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

def run_knn():
    st.title("K-Nearest Neighbors (KNN) Classification")

    # Generate sample data
    X, y = make_classification(n_samples=300, n_features=2, n_informative=2, 
                           n_redundant=0, n_clusters_per_class=1, random_state=42)


    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Get user input for K
    k = st.slider("Select Number of Neighbors (K)", 1, 10, 3)

    # Train KNN model
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)

    # Predict
    y_pred = knn.predict(X_test)

    # Plot the data
    fig, ax = plt.subplots()
    scatter = ax.scatter(X_test[:, 0], X_test[:, 1], c=y_pred, cmap='coolwarm', edgecolor='k')
    ax.set_title(f"KNN Classification (K={k})")
    ax.set_xlabel("Feature 1")
    ax.set_ylabel("Feature 2")
    
    # Display plot
    st.pyplot(fig)
