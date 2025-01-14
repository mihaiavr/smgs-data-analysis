
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load data
data_path = 'dataIN/employment_dataset_raw.xlsx'
sheet_name = 'Sheet1'

data = pd.read_excel(data_path, sheet_name=sheet_name)

# Clean and preprocess data
data.columns = data.columns.str.strip()  # Remove leading/trailing whitespace
data['Resurse de munca'] = data['Resurse de munca'].str.replace(',', '.').astype(float)
numerical_cols = [
    'Accidente colective de munca (dummy variable)',
    'Biblioteci',
    'Castigul salarial nominal mediu net lunar',
    'Numarul mediu al salariatilor',
    'Resurse de munca',
    'Unitatile de invatamant'
]
data_numeric = data[numerical_cols]
data_numeric_imputed = data_numeric.fillna(data_numeric.mean())

# Standardize data
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data_numeric_imputed)

# Perform PCA
pca = PCA(n_components=2)
pca_result = pca.fit_transform(data_scaled)

# Create PCA DataFrame
pca_df = pd.DataFrame(pca_result, columns=['PC1', 'PC2'])
pca_df['Region'] = data['Macroregiuni, regiuni de dezvoltare si judete']

# Plot PCA results
plt.figure(figsize=(12, 8))
for i in range(len(pca_df)):
    plt.scatter(pca_df.loc[i, 'PC1'], pca_df.loc[i, 'PC2'], alpha=0.7)
    plt.text(pca_df.loc[i, 'PC1'] + 0.1, pca_df.loc[i, 'PC2'], pca_df.loc[i, 'Region'], fontsize=8)
plt.title('PCA Results with Region Labels')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.grid(True)
plt.savefig('dataOUT/PCA_Scatter_Plot.png')
plt.close()

# Save PCA results
pca_df.to_csv('dataOUT/PCA_results.csv', index=False)

print("PCA analysis completed. Results saved in 'dataOUT' folder.")