import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load cleaned dataset from dataOUT
df = pd.read_csv("../dataOUT/employment_data_cleaned.csv")

# Standardize features
features = ["Libraries", "Avg_Salary", "Num_Employees", "Workforce", "Education_Units"]
X_scaled = StandardScaler().fit_transform(df[features])

# Apply PCA
pca = PCA(n_components=2)
df_pca = pd.DataFrame(pca.fit_transform(X_scaled), columns=["PC1", "PC2"])

# Apply KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=42)
df["Cluster"] = kmeans.fit_predict(X_scaled)

# Save results in dataOUT
df.to_csv("../dataOUT/employment_clusters.csv", index=False)

# Plot Clusters
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df_pca["PC1"], y=df_pca["PC2"], hue=df["Cluster"], palette="Set1")
plt.title("Clusters of Employment Data")
plt.show()

print("✅ Clustering results saved in dataOUT/")
