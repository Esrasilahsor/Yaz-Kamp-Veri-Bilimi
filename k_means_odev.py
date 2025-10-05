#!/usr/bin/env python
# coding: utf-8


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


data = pd.read_csv('dava.csv')
data

X = data.iloc[:, 1:] 

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("Veri başarıyla ölçeklendirildi.")

wcss = []
# K = 1'den 10'a kadar deneme yapıyoruz
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42, n_init=10) 
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_) # inertia_ = WCSS

plt.figure(figsize=(9, 6))
plt.plot(range(1, 11), wcss, marker='o', linestyle='--')
plt.title('Elbow Metodu ile Optimal K Değerini Bulma')
plt.xlabel('Küme Sayısı (K)')
plt.ylabel('WCSS (Küme İçi Hata Kareleri Toplamı)')
plt.grid(True)
plt.show()


optimal_k = 3 

kmeans_final = KMeans(n_clusters=optimal_k, init='k-means++', random_state=42, n_init=10)
kmeans_final.fit(X_scaled)

data['Cluster'] = kmeans_final.labels_

plt.figure(figsize=(10, 6))
plt.scatter(data['Case Duration (Days)'], data['Legal Fees (USD)'], 
            c=data['Cluster'], cmap='viridis', s=50, alpha=0.7)

centers_scaled = kmeans_final.cluster_centers_
centers_original = scaler.inverse_transform(centers_scaled) 

plt.scatter(centers_original[:, 0], centers_original[:, 2], 
            marker='X', s=250, color='red', label='Küme Merkezleri') 

plt.title(f'K-Means Kümeleme Sonuçları (K={optimal_k} - Ölçekli Veri)')
plt.xlabel('Dava Süresi (Gün)')
plt.ylabel('Hukuk Maliyetleri (USD)')
plt.legend()
plt.grid(True)
plt.show()




