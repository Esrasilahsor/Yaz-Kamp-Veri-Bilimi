#!/usr/bin/env python
#coding: utf-8


import pandas as pd
import numpy as np

data = pd.read_csv('country.csv')
data
print(data.columns.tolist())


# ## 1. Görev : Nüfusa Göre Azalan Sırada Sıralama:


nufusa_gore_siralama= data.sort_values("Population" ,ascending=False)
print("Nüfusa Göre Sıralama:\n" ,nufusa_gore_siralama)


# ## 2. Görev: GDP per capita sütununa göre ülkeleri artan sırada sıralamak(Kişi başına düşen Gayri Safi Yurtiçi Hasıla).

ulkeleri_siralama=data.sort_values("GDP ($ per capita)", ascending=True)
print("Kişi başına düşen Gayri Safi Yurtiçi Hasıla'ya Göre Sıralama:\n",ulkeleri_siralama)


# ## 3. Görev: Population sütunu 10 milyonun üzerinde olan ülkeleri seçmek.

nufus_filtreleme= data[data["Population"]>10000000]
print("Population sütunu 10 milyonun üzerinde olan ülkeler:\n",nufus_filtreleme)


# ## 4. Görev: Literacy (%) sütununa göre ülkeleri sıralayıp, en yüksek okur-yazarlık oranına sahip ilk 5 ülkeyi seçmek.

okur_yazarlık_oranı= data.sort_values("Literacy (%)", ascending=False)
print("En yüksek okur-yazarlık oranına sahip ilk 5 ülke:\n",okur_yazarlık_oranı.head())


# ## 5. Görev:  Kişi Başı GSYİH 10.000'in Üzerinde Olan Ülkeleri Filtreleme: GDP ( per capita) sütunu 10.000'in üzerinde olan ülkeleri seçmek.

gdp_filtreleme= data[data["GDP ($ per capita)"]>10000]
print("GDP ( per capita) sütunu 10.000'in üzerinde olan ülke:\n",gdp_filtreleme)


# ## Görev 6 : En Yüksek Nüfus Yoğunluğuna Sahip İlk 10 Ülkeyi Seçme:
# Pop. Density (per sq. mi.) sütununa göre ülkeleri sıralayıp, en yüksek nüfus yoğunluğuna sahip ilk 10 ülkeyi seçmek.

en_yuksek_nufus_yogunlugu= data.sort_values("Pop. Density (per sq. mi.)",ascending=False)
print("En Yüksek Nüfus Yoğunluğuna Sahip İlk 10 Ülke:\n",en_yuksek_nufus_yogunlugu.head(10))
