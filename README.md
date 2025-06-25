# CodeClauseInternship-Customer-Segmentation-Tool

A golden-level data science project for segmenting customers using clustering techniques and an interactive user interface. Built with Streamlit and scikit-learn as part of the **CodeClause Data Science Internship**.

## What This Project Does

- Creates a user-friendly interface for customer data input using **Streamlit**.
- Accepts CSV uploads or uses sample data with customer demographics and behavior.
- Applies **K-Means Clustering** to segment customers into meaningful groups.
- Allows users to select which features (e.g., Age, Income, Spending Score) to use for segmentation.
- Visualizes cluster groups with **scatter plots** based on selected features.

## Technologies Used

- **Programming Language**: Python  
- **Libraries & Tools**:
  - [Streamlit](https://streamlit.io/) – for building the interactive UI
  - [Pandas](https://pandas.pydata.org/) – for data manipulation
  - [Scikit-learn](https://scikit-learn.org/) – for clustering with K-Means
  - [Matplotlib](https://matplotlib.org/) & [Seaborn](https://seaborn.pydata.org/) – for data visualization

## Project Structure

### 1. Upload or Load Sample Data
- Users can upload a `.csv` file with customer data
- Or use a default sample file included in the project (`sample_customers.csv`)

### 2. Feature Selection
- Automatically detects numerical columns
- Users select features (like Age, Income) for clustering

### 3. Select Number of Clusters
- Choose the value of **K** (number of clusters) using a slider

### 4. Run K-Means Clustering
- KMeans algorithm groups customers based on selected features
- Assigns each customer to a cluster

### 5. View Results
- View dataset with cluster labels
- Visualize customer segments using scatter plots

## How to Run This Project

**Clone the Repository**:
```bash
git clone https://github.com/Gowry11/CodeClauseInternship-Customer-Segmentation-Tool-2-.git

