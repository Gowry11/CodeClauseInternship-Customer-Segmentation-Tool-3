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

### 1. Clone the Repository**:
```bash
git clone https://github.com/Gowry11/CodeClauseInternship-Customer-Segmentation-Tool-2-.git
```
### 2. Navigate to the Project Folder:
```bash
cd CodeClauseInternship-Customer-Segmentation-Tool
```
### 3. Install Required Libraries:
```bash
pip install -r requirements.txt
```
### 4. Run the Streamlit App:
```bash
streamlit run app.py
```
The app will open in your browser where you can upload data, choose features, and explore the clustering results.

## Sample Data
Included in the repository under:
```bash
data/sample_customers.csv
```
This file contains example customer data with fields like:  
- CustomerID  
- Age  
- Annual Income  
- Spending Score

## Output Preview  
- Upload customer CSV file  
- Choose features to cluster  
- Choose number of clusters (K)  
- View table with cluster labels  
- View scatter plot of customer segments

## Demo Video
🎥 [Include your LinkedIn video demo link here when ready]

## Developed By  
Gowry P P
