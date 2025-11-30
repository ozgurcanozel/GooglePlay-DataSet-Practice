import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("googleplaystore.csv")
print(df.head())
print(df.columns) # columns of head
print(df.info())
print(df.describe()) # numerics
print("-"*50)


#### missing data ###
print(df.isnull().sum())

## string convert to integer for Reviews
# df["Reviews"] = df["Reviews"].astype(int) her sey uygun degil

print(df["Reviews"].str.isnumeric().sum()) # kac tanesi numeric diye baktik

print(df[~df["Reviews"].str.isnumeric()]) # numeric olmayanlari gosteriyor

df_clean = df.copy() # data temizligi icin ana df yi bozmamak icin yeni actik

df_clean = df_clean.drop(df_clean.index[10472])

df_clean["Reviews"] = df_clean["Reviews"].astype(int)
print(df_clean.info())


# print(df_clean["Size"].value_counts())
# print(df_clean["Size"].unique())

"""Her seyi kilobayt seklinde yazacagiz"""

df_clean["Size"] = df_clean["Size"].str.replace("M", "000")
df_clean["Size"] = df_clean["Size"].str.replace("k", "")
df_clean["Size"] = df_clean["Size"].replace("Varies with device", np.nan)
print(df_clean["Size"].unique())

df_clean["Size"] = df_clean["Size"].astype(float)
print(df_clean.isnull().sum())
print(df_clean.info())

print(df_clean.tail())


"""Installs kismina bakacagiz"""

print(df_clean["Installs"].value_counts()) # number of download
print(df_clean["Price"].value_counts())

chars_to_remove = ["+",",","$"]
cols_to_clean = ["Installs", "Price"]

for item in chars_to_remove:
    for cols in cols_to_clean:
        df_clean[cols] = df_clean[cols].str.replace(item, "")

print(df_clean["Price"].unique())
print(df_clean["Installs"].unique())

df_clean["Price"] = df_clean["Price"].astype(float)
df_clean["Installs"] = df_clean["Installs"].astype(int)

print(df_clean.info())
print(df_clean.describe())

print(df_clean.head())

print(df_clean["Last Updated"].unique())
df_clean["Last Updated"] = pd.to_datetime(df_clean["Last Updated"])
# print(df_clean["Last Updated"].head())

df_clean["Day"] = df_clean["Last Updated"].dt.day # cevirdikten sonra yapacagiz
df_clean["Month"] = df_clean["Last Updated"].dt.month # cevirdikten sonra yapacagiz
df_clean["Year"] = df_clean["Last Updated"].dt.year # cevirdikten sonra yapacagiz

print(df_clean.head())

print(df_clean.info())