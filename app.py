# Import necessary libraries
import streamlit as st           # for UI
import pandas as pd              # to work with data
from sklearn.cluster import KMeans   # for clustering
import matplotlib.pyplot as plt  # to make charts
import seaborn as sns            # prettier charts

# Set the page layout
st.set_page_config(page_title="Customer Segmentation Tool", layout="wide")

# Title and intro
st.title("🧑‍💼Customer Segmentation Tool")
st.write("Upload customer data or use sample data to analyze customer segments using K-Means clustering.")

# 📤 File upload option
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

# ✅ Load uploaded data or use sample
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("Uploaded file successfully!")
else:
    df = pd.read_csv("data/sample_customers.csv")
    st.info("Using default sample data.")

# 👀 Show preview of the data
st.write("### Preview of Dataset:")
st.dataframe(df.head())

# 🧹 Select columns for clustering
numeric_cols = df.select_dtypes(include='number').columns.tolist()

# 🔘 Choose which features to use
selected_features = st.multiselect("Select features for clustering:", numeric_cols, default=numeric_cols[1:])

if len(selected_features) >= 2:
    X = df[selected_features]

    # 🎯 Choose number of clusters
    k = st.slider("Select number of clusters (K):", 2, 10, 3)

    # 🤖 Apply KMeans
    kmeans = KMeans(n_clusters=k, random_state=42)
    df['Cluster'] = kmeans.fit_predict(X)

    # 📊 Show data with cluster labels
    st.write("### Data with Cluster Labels:")
    st.dataframe(df)

    # 🖼️ Show scatter plot
    st.write("### Cluster Visualization:")
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x=selected_features[0], y=selected_features[1], hue='Cluster', palette='tab10', ax=ax)
    st.pyplot(fig)

else:
    st.warning("Please select at least two features for clustering.")
