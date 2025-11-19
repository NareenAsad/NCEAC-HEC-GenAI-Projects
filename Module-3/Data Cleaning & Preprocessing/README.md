# 🏡 Housing Dataset — Cleaning & Preprocessing

This folder contains the complete data cleaning and preprocessing workflow for the **Housing Prices Dataset** from Kaggle.
The goal of this notebook is to prepare the dataset for machine learning by handling missing values, encoding categorical features, scaling numeric features, and performing train/validation/test splits.

---

## 📂 Folder Contents

| File                                     | Description                                                                |
| ---------------------------------------- | -------------------------------------------------------------------------- |
| **housing_cleaning.ipynb**               | Jupyter/Colab notebook containing all data cleaning & preprocessing steps. |
| **Housing.csv**                          | Raw dataset downloaded from Kaggle.                                        |
| **housing_cleaned.csv**                  | Cleaned version of the dataset after preprocessing.                        |                                          |

---

## 🧼 Data Cleaning Steps

The notebook performs the following:

### **1. Load and Inspect Data**

* `.head()`, `.info()`, `.describe()`
* Check column types, unique values, and data shape

### **2. Column Normalization**

* Convert column names to lowercase
* Remove spaces
* Standardize yes/no columns → 1/0

### **3. Handling Missing Values**

* Numeric: median imputation
* Categorical: mode imputation

### **4. Encoding Categorical Features**

* **furnishingstatus** treated as **ordinal**
  (unfurnished < semi-furnished < furnished)
* Yes/No columns converted to binary
* One-hot encoding used only if required

### **5. Outlier Detection**

* IQR method used to identify extreme values
* Optional filtering of unrealistic entries

### **6. Feature Scaling**

* StandardScaler for numeric columns
* Fit only on training data (prevents data leakage)

### **7. Dataset Splitting**

* Train (70%)
* Validation (15%)
* Test (15%)

### **8. Saving Outputs**

* Cleaned CSV
* Transformed training/validation/test arrays

---

## 🛠️ Requirements

The notebook works in **Google Colab** and requires:

```
pandas
numpy
scikit-learn
matplotlib
```

(No additional installation needed in Colab.)

---

## 🚀 How to Use

1. Upload `Housing.csv` into the runtime
2. Open `housing_cleaning.ipynb` in Google Colab
3. Run all cells
4. Use cleaned data or transformed `.npy` files to train machine-learning models

---

## 📄 Dataset Source

Kaggle — Housing Prices Dataset
(Uploaded by: **Yasser**)

---

## 📌 Notes

* This project is beginner-friendly and demonstrates proper preprocessing workflows.
* The cleaned dataset is ready for regression models such as Linear Regression, RandomForest, XGBoost, and Neural Networks.
