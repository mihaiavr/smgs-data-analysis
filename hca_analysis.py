
import pandas as pd
import os
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# Load PCA results
pca_results_path = 'dataOUT/PCA_results.csv'
pca_results = pd.read_csv(pca_results_path)

# Perform Hierarchical Cluster Analysis (HCA)
linkage_matrix = linkage(pca_results[['PC1', 'PC2']], method='ward')

# Plot HCA dendrogram
plt.figure(figsize=(12, 8))
dendrogram(linkage_matrix, labels=pca_results['Region'].tolist(), leaf_rotation=90, leaf_font_size=10)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Regions')
plt.ylabel('Distance')
plt.savefig('dataOUT/HCA_Dendrogram.png')
plt.close()

print("HCA analysis completed. Dendrogram saved in 'dataOUT' folder.")