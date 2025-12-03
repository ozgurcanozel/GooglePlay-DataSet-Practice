# 📊 Google Dataset Practice  
Comprehensive Data Cleaning & Exploratory Data Analysis (EDA) Project

This project was created as part of my data science learning journey, using a real dataset to perform an extensive EDA (Exploratory Data Analysis) on **Google Play Store applications**. The project includes detailed data cleaning, data transformation, visualization, and category-based analysis.

---

## 📁 Dataset  
Dataset used: **googleplaystore.csv**

This dataset contains various features such as app names, categories, size, price, installs, rating, review count, and last update dates.

---

## 🧹 Data Cleaning

Data cleaning steps performed in the project:

### ✔ Detection of missing values  
- Missing data analysis using `df.isnull().sum()`

### ✔ Cleaning the Reviews column  
- Detection of non-numeric values  
- Deletion of problematic index  
- Converting `Reviews` to `int`

### ✔ Transformation of the Size column  
- `"M"` → `"000"`  
- `"k"` → `""`  
- `"Varies with device"` → `NaN`  
- Conversion of all values to `float`  
  → Sizes were converted into kilobyte format.

### ✔ Installs & Price column cleaning  
Character removal:
- Removed `+`, `,`, `$`  
- Converted `Installs` → `int`, `Price` → `float`

### ✔ Last Updated column  
- Converted into datetime format  
- Extracted additional features: **Day, Month, Year**

### ✔ Duplicate App cleaning  
- Removed duplicated applications (`keep='first'`)

### ✔ Android Version column cleaning  
- Removed `"and up"` text  
- `"Varies with device"` → `NaN`  
- Corrected format inconsistencies

---

## 📊 Exploratory Data Analysis (EDA)

After cleaning the dataset, the following analyses were performed:

### 🔹 Distribution of numerical features  
- Histogram + density plots using `sns.kdeplot()`  
- Analyzed features: Rating, Size, Price, Reviews, Installs

### 🔹 Application distribution by categories  
- Content Rating  
- Type (Free / Paid)

### 🔹 Total installs by category  
- Grouping + total installs bar chart  
- Top 10 categories with the highest install counts

### 🔹 Top 5 most installed apps by category  
- Categories analyzed: GAME, COMMUNICATION, TOOLS, PRODUCTIVITY, SOCIAL

### 🔹 Apps with the highest rating (Rating = 5.0)  
- Category + Installs + App analysis

### 🔹 Genre Target Encoding  
- Average installs calculated for each genre  
- New feature created: **Genres Encoded**

---

## 📚 Technologies Used
- **Python 3.x**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**

---


![Distribution Plots]()
<img width="2245" height="854" alt="Screenshot 2025-12-03 083239" src="https://github.com/user-attachments/assets/102f4e14-2ccf-44c7-a087-8ab07e96172d" />


![Top Categories]()
<img width="1447" height="743" alt="Screenshot 2025-12-03 083305" src="https://github.com/user-attachments/assets/4e70b412-d527-48a6-8b79-c11396b3a28c" />



![Top 5 Apps]()
<img width="2559" height="1279" alt="Screenshot 2025-12-03 083321" src="https://github.com/user-attachments/assets/23d922d0-5349-41bf-ab50-919fc9d54175" />



