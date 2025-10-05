#!/usr/bin/env python
# coding: utf-8


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
from sklearn.tree import plot_tree
from sklearn.model_selection import train_test_split



data = pd.read_csv('dava_sonuclari.csv')
data.head()


print("Eksik Değerler:\n",data.isnull().sum())

data.info()

X = data.drop("Outcome",axis=1)
y = data["Outcome"]

X = pd.get_dummies(X, columns=['Case Type'], drop_first=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

print("Eğitim veri sayısı:", X_train.shape[0])
print("Test veri sayısı:", X_test.shape[0])

model = DecisionTreeClassifier(random_state=0, max_depth=5)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Doğruluk:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1-Score:", f1_score(y_test, y_pred))
print("\nSınıflandırma Raporu:")
print(classification_report(y_test, y_pred))

plt.figure(figsize=(20,10))
plot_tree(model, filled=True, feature_names=X.columns, 
          class_names=['Kaybetti', 'Kazandı'], rounded=True)
plt.show()