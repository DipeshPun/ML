import streamlit as st
import knn as knn_module
import kmeans as kmeans_module

# Streamlit UI
st.title("Machine Learning Algorithms")
st.subheader("Choose an algorithm to visualize")

# Buttons to choose between KNN and K-Means
option = st.radio("Select Algorithm", ("KNN", "K-Means"))

if option == "KNN":
    knn_module.run_knn()
elif option == "K-Means":
    kmeans_module.run_kmeans()
