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


                    ###### EDA (Exploratory data analysis) ######

print(df_clean[df_clean.duplicated('App')].shape)

df_clean = df_clean.drop_duplicates(subset=['App'], keep='first')
print(df_clean.info())
print(df_clean.shape)

numeric_features = [feature for feature in df_clean.columns if df_clean[feature].dtype != "O"]
categorical_features = [feature for feature in df_clean.columns if df_clean[feature].dtype == "O"]

print(numeric_features)
print(categorical_features)

# print(df_clean["Android Ver"].dtype) # O
# print(df_clean["Day"].dtype)


# plt.figure(figsize = (15,10))
#
# for i in range(0, len(numeric_features)):
#     plt.subplot(5, 3, i+1) # 5 satir 3 kolonluk
#     sns.kdeplot(x=df_clean[numeric_features[i]],color = "b", fill = True) # dagilim ciziyor
#     plt.xlabel(numeric_features[i])
#     plt.tight_layout()
# plt.show()
#
# # free or paid & for who
# plt.figure(figsize = (15,4))
#
# category = ["Type", "Content Rating"]

# for i in range(0, len(category)):
#     plt.subplot(1, 2, i+1) # 5 satir 3 kolonluk
#     sns.countplot(x=df_clean[category[i]],color = "b", fill = True)
#     plt.xlabel(category[i])
#     plt.tight_layout()
# plt.show()

print(df_clean["Category"].value_counts())

## top app categories by installment

print(df_clean.tail())
df_cat_installs = (df_clean.groupby(["Category"])["Installs"].sum().sort_values(ascending=False).reset_index())
df_cat_installs["Installs"] = df_cat_installs["Installs"]/1000000000
print(df_cat_installs)

## top 10 categories by install

df2 = df_cat_installs.head(10) # ilk 10 u aliyor
plt.figure(figsize = (10,5))

sns.barplot(x = "Installs", y = "Category", data = df2)
plt.show()

