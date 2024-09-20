from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
import pandas as pd
import os

pth = "D:\\10. SRH_Academia\\1. All_Notes\\2. Semester 2\\3. Artificial Intelligence\\Project\\DATA\\Data\\features_30_sec.csv"
pca_nme = "PCA_" + os.path.basename(pth)
pca_path = os.path.join(os.path.dirname(pth), pca_nme)

df = pd.read_csv(pth)
df2 = df.drop(['filename', 'label'], axis='columns')
print(df.head())
print(df2.head())
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(df2)
pca_df = pd.DataFrame(data=principalComponents, columns=['principal component 1', 'principal component 2'])
df = pd.concat([pca_df, df], axis=1)
df.to_csv(path_or_buf=pca_path, index=False)

df = df.drop(['filename'], axis='columns')



