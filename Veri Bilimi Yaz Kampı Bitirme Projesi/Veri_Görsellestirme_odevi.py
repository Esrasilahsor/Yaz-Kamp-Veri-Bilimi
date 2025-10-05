#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('50_Startups.csv')
data.head()


# ## 1.GÖREV : R&D Harcaması ve Kâr Arasındaki İlişki (Scatter Plot): Ar-Ge harcamaları ile kâr arasındaki ilişkiyi gösteren bir dağılım grafiği.

# In[11]:

plt.scatter(
    x= data["R&D Spend"],
    y= data["Profit"]
)
plt.title("R&D Harcaması ve Kâr Arasındaki İlişki")
plt.xlabel("Ar-Ge Harcaması")
plt.ylabel("Kâr")
plt.grid(True)
plt.show()


# ## 2.GÖREV: Yönetim Harcamaları ve Kâr Arasındaki İlişki (Scatter Plot): Yönetim harcamaları ile kâr arasındaki ilişkiyi gösteren bir dağılım grafiği.

plt.scatter(
    x= data["Administration"],
    y= data["Profit"]
)
plt.title("Yönetim Harcamaları ve Kâr Arasındaki İlişki")
plt.xlabel("Yönetim Harcamaları")
plt.ylabel("Kâr")
plt.grid(True)
plt.show()


# ## 3. GÖREV: Eyaletlere Göre Ortalama Kâr (Bar Chart): Farklı eyaletlerdeki startup'ların ortalama kârlarını karşılaştıran bir çubuk grafik.


ortalama_kar = data.groupby('State')['Profit'].mean()

plt.bar(ortalama_kar.index, ortalama_kar.values)
plt.title("Eyaletlere Göre Ortalama Kâr")
plt.xlabel("Eyalet")
plt.ylabel("Ortalama Kâr")
plt.show()


# ## 4. GÖREV: Harcama Türlerinin Karşılaştırması (Boxplot): R&D, yönetim ve pazarlama harcamalarının dağılımını karşılaştıran bir kutu grafiği.


harcama = [
    data['R&D Spend'],
    data['Administration'],
    data['Marketing Spend']
]
plt.title("Harcama Türlerinin Karşılaştırması")
plt.boxplot(harcama)
plt.ylabel('Harcama Tutarı)')
plt.xticks(
    [1, 2, 3], 
    ['R&D Spend', 'Yönetim Harcaması', 'Pazarlama Harcaması'] # Bunları kendi veri setinizdeki tam kolon adlarıyla değiştirin!
) 
plt.show()

