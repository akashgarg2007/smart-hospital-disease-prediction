# 🏥 Smart Hospital & Disease Prediction System

A Machine Learning based Smart Hospital Management and Disease Prediction System built with Python and Flask.

The application provides disease prediction for multiple health conditions through a simple web interface and stores prediction records for hospital management.

## 🚀 Features

- 🏥 Smart Hospital Dashboard
- 🩺 Disease Prediction System
- 🩸 Diabetes Prediction
- ❤️ Heart Disease Prediction
- 🧠 Stroke Prediction
- 🫘 Kidney Disease Prediction
- 🫀 Liver Disease Prediction
- 👨‍⚕️ Patient Management
- 📊 Prediction Probability
- 📅 Prediction History
- 💾 SQLite Database
- 📓 Machine Learning Notebooks
- 📄 Model Evaluation Reports
- 🌐 Flask Web Application

## 🧠 Machine Learning Models

The project contains trained machine learning models for:

| Disease | Model |
|---|---|
| Diabetes | Classification Model |
| Heart Disease | Classification Model |
| Stroke | Classification Model |
| Kidney Disease | Classification Model |
| Liver Disease | Classification Model |

Each prediction module uses the corresponding trained model and preprocessing/scaling components.

## 🛠️ Tech Stack

### Programming
- Python

### Machine Learning
- Scikit-learn
- NumPy
- Pandas

### Web Development
- Flask
- HTML
- CSS
- JavaScript

### Database
- SQLite

### Development Tools
- Jupyter Notebook
- VS Code
- Git
- GitHub

## 📁 Project Structure

```text
smart-hospital-disease-prediction/
│
├── data/
│   ├── hospital_patient_records.csv
│   └── hospital_patient_records_cleaned.csv
│
├── database/
│   └── health.db
│
├── models/
│   ├── diabetes_model.pkl
│   ├── heart_model.pkl
│   ├── heart_scaler.pkl
│   ├── kidney_model.pkl
│   ├── kidney_scaler.pkl
│   ├── Liver_model.pkl
│   ├── Liver_scaler.pkl
│   ├── stroke_model.pkl
│   ├── stroke_scaler.pkl
│   └── scaler.pkl
│
├── notebook/
│   ├── EDA_Preprocessing.ipynb
│   ├── diabetes_model.ipynb
│   ├── Heart_Disease_Model.ipynb
│   ├── kidney_Disease_Model.ipynb
│   ├── Liver_Disease_Model.ipynb
│   └── Stroke_Model.ipynb
│
├── reports/
│   ├── AI_Health_Report.pdf
│   ├── Diabetes_Report.pdf
│   └── Heart_Disease_Report.pdf
│
├── static/
│   ├── css/
│   ├── images/
│   └── js/
│
├── templates/
│   ├── dashboard.html
│   ├── diabetes.html
│   ├── heart.html
│   ├── kidney.html
│   ├── liver.html
│   ├── stroke.html
│   └── index.html
│
├── app.py
├── requirements.txt
└── README.md


## 🔄 Machine Learning Workflow
1. Data Collection
        ↓
2. Data Cleaning & Preprocessing
        ↓
3. Exploratory Data Analysis (EDA)
        ↓
4. Feature Engineering
        ↓
5. Train-Test Split
        ↓
6. Model Training
        ↓
7. Model Evaluation
        ↓
8. Hyperparameter Tuning
        ↓
9. Model Saving
        ↓
10. Flask Web Application
        ↓
11. Disease Prediction
