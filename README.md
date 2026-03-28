# 🔐 Intelligent Login Risk Analyzer

## 📌 Project Overview

The **Intelligent Login Risk Analyzer** is a cybersecurity-focused data analytics and machine learning project designed to detect suspicious user login behavior.

The system analyzes login activity based on:

* time of login
* location
* device/browser
* login success/failure

and identifies potentially risky or anomalous login attempts using both **rule-based logic** and **machine learning techniques**.

---

## 🎯 Project Objectives

The main objectives of this project are:

* Detect unusual login behavior patterns
* Identify potential security threats such as brute-force attempts
* Build a risk scoring mechanism for login events
* Apply anomaly detection using machine learning
* Simulate a real-world login security monitoring system

---

## 🧠 Key Features

* ✅ Rule-based anomaly detection
* ✅ Feature engineering for behavioral analysis
* ✅ Risk scoring system (Low / Medium / High)
* ✅ Machine learning using Isolation Forest
* ✅ End-to-end detection pipeline
* ✅ System testing with multiple scenarios
* ✅ Demonstration-ready notebook

---

## 📊 Dataset Description

The project uses a synthetic dataset containing **300 login records** with the following structure:

| Column   | Description              |
| -------- | ------------------------ |
| user     | User ID                  |
| time     | Login time               |
| location | Login location           |
| device   | Browser or mobile        |
| status   | Login success or failure |

---

## ⚙️ Tools & Technologies

* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* Scikit-learn (Isolation Forest)
* Jupyter Lab

---

## 🧱 Project Structure

```
Intelligent Login Risk Analyzer/
│
├── data/                     # Dataset
├── notebooks/               # Project notebooks
│   ├── 01_environment_setup.ipynb
│   ├── 02_dataset_exploration.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_model_training.ipynb
│   ├── 05_model_evaluation.ipynb
│   ├── 06_detection_pipeline.ipynb
│   ├── 07_system_testing.ipynb
│   └── 08_project_demonstration.ipynb
│
├── outputs/                 # Generated outputs
├── models/                  # (Optional future use)
└── README.md
```

---

## 🔍 Methodology

### 1. Data Exploration

* Analyzed login patterns
* Identified failed login behavior
* Explored location, device, and time distributions

### 2. Feature Engineering

Created meaningful features such as:

* `is_failed`
* `is_night_login`
* `is_high_risk_location`
* `is_suspicious_device`

---

### 3. Risk Scoring System

A rule-based scoring system assigns weights to suspicious behaviors:

* Failed login → High weight
* Night login → Medium weight
* High-risk location → High weight
* Suspicious device → Low weight

---

### 4. Machine Learning Model

* Algorithm: **Isolation Forest**
* Type: Unsupervised anomaly detection
* Purpose: Detect unusual login patterns

---

### 5. Detection Pipeline

The system:

1. Receives login input
2. Generates features
3. Calculates risk score
4. Applies ML model
5. Produces anomaly decision

---

### 6. System Testing

Multiple scenarios were tested:

* normal login
* failed login
* night-time login
* high-risk location login
* combined suspicious cases

---

## 📈 Results & Insights

* Failed logins are strong indicators of suspicious activity
* Night-time login patterns may indicate abnormal behavior
* Certain locations show higher risk patterns
* Combined signals significantly increase risk score
* The model successfully identifies anomalous login behavior

---

## 🚨 Example Scenario

> A user logs in from Dhaka at 10:00 AM and later from Russia at 3:00 AM using a mobile device → flagged as high-risk anomaly.

---

## 🚀 Future Improvements

* Real-time detection system
* API integration (FastAPI)
* Interactive dashboard (Streamlit)
* Advanced ML models
* Geo-distance based anomaly detection
* Alert system (email/notification)

---

## 💼 Project Value

This project demonstrates:

* Cybersecurity awareness
* Data analysis and feature engineering
* Machine learning application
* System design thinking
* End-to-end pipeline development

---

## ⚠️ Important Note

This project uses a synthetic dataset and unsupervised learning.
Detected anomalies represent **suspicious patterns**, not confirmed attacks.

---

## 👨‍💻 Author

**Niher Halder**
ChatGPT Plus Workspace
Email: [niher.tech@gmail.com](mailto:niher.tech@gmail.com)

---

## ⭐ Final Remark

This project is designed as a **portfolio-level cybersecurity system prototype**, demonstrating how AI and data analysis can be applied to real-world login security problems.
