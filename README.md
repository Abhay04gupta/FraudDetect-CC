## 🧠 Credit Card Fraud Detection System

### 📌 Overview

This project aims to detect fraudulent credit card transactions using machine learning techniques. Real-world datasets are highly imbalanced, with very few fraud cases compared to genuine transactions. To overcome this challenge, **undersampling** and **oversampling** techniques were implemented to improve model generalization and accuracy.

### 🚀 Key Features

* Preprocessing of imbalanced datasets using **SMOTE** and **Random Under-Sampling**.
* Feature analysis on anonymized transaction variables *(V1–V28)* and `Amount`.
* Multiple classification models trained and compared for performance.
* Optimized model saved for real-time fraud prediction deployment.

### ⚙️ Machine Learning Models Used

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier
* XGBoost Classifier

### 🧩 Dataset

The dataset used contains anonymized credit card transactions, with features `V1–V28` derived from PCA transformations and an `Amount` column. The target variable `Class` indicates whether a transaction is fraudulent (1) or genuine (0).

### 🧱 Project Workflow

1. **Data Loading and Preprocessing**

   * Handled missing values and scaled numerical columns.
   * Balanced data using **SMOTE** and **undersampling** methods.
2. **Model Training and Evaluation**

   * Trained multiple classifiers and compared metrics.
   * Used accuracy, precision, recall and f1-score for evaluation.
3. **Model Saving and Deployment**

   * Exported best-performing model as `credit_card_model.pkl`.
   * Integrated into Streamlit web app for user-friendly prediction.

### 💡 How to Run the Project

1. Clone the repository

   ```bash
   git clone https://github.com/username/Credit-Card-Fraud-Detection-System.git
   cd Credit-Card-Fraud-Detection-System
   ```
2. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app

   ```bash
   streamlit run app.py
   ```

### 🧾 Input Format

The Streamlit web app accepts **29 inputs** — anonymized features (`V1–V28`) and `Amount`, then outputs whether the transaction is **Fraudulent** or **Genuine**.

### 🏆 Results & Insights

* Addressed **class imbalance** to significantly boost fraud recall.
* Achieved **high accuracy and reliability** across multiple ML models.
* Demonstrated real-world fraud detection pipeline deployable in finance applications.

Would you like me to include a **“Demo Streamlit app section”** (with screenshot placeholder and sample inputs table)? It’ll make your README look even more professional for GitHub.
