# Practical 6: K-Means and Hierarchical Clustering
# Dataset required: sales_data_sample.csv

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster

# 1. Load dataset
df = pd.read_csv("sales_data_sample.csv", encoding="latin1", on_bad_lines="skip")
print("Dataset shape:", df.shape)
print(df.head())

# 2. Select numerical features and handle missing values
X = df.select_dtypes(include=["int64", "float64"]).copy()
X = X.fillna(X.median(numeric_only=True))
print("\nFeatures used for clustering:")
print(X.head())

# 3. Standardize data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Elbow method to choose number of clusters
wcss = []
k_values = range(1, 11)
for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(6, 4))
plt.plot(list(k_values), wcss, marker="o")
plt.title("Elbow Method")
plt.xlabel("Number of clusters (k)")
plt.ylabel("Inertia (WCSS)")
plt.grid(True)
plt.tight_layout()
plt.show()

# 5. K-Means clustering (using 3 clusters, as in the practical)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df["KMeans_Cluster"] = kmeans.fit_predict(X_scaled)

print("\nK-Means cluster centers (scaled values):")
print(kmeans.cluster_centers_)
print("\nCluster counts:")
print(df["KMeans_Cluster"].value_counts())

# Visualize clusters if these columns exist
if "SALES" in df.columns and "PRICEEACH" in df.columns:
    sns.scatterplot(data=df, x="SALES", y="PRICEEACH", hue="KMeans_Cluster", palette="viridis")
    plt.title("K-Means Clustering")
    plt.tight_layout()
    plt.show()

# 6. Hierarchical clustering
# Ward linkage on standardized numeric features
linked = linkage(X_scaled, method="ward")

plt.figure(figsize=(12, 5))
dendrogram(linked, truncate_mode="lastp", p=30)
plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("Sample / Cluster")
plt.ylabel("Distance")
plt.tight_layout()
plt.show()

df["Hierarchical_Cluster"] = fcluster(linked, t=3, criterion="maxclust")
print("\nHierarchical cluster counts:")
print(df["Hierarchical_Cluster"].value_counts())
