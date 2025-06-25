# 🏪 Pharmaceutical Store Sales Forecasting

Welcome to **Rossmann Sales Forecasting**, a project developed at **NextHikes IT Solutions** to predict daily sales across multiple pharmaceutical retail stores using machine learning and deep learning techniques. This project not only predicts sales 6 weeks ahead but also provides a user-friendly web interface for store managers.

---

## 📌 Project Objective

Forecast daily sales across various Rossmann stores by:
- Understanding customer purchasing behavior
- Building accurate machine learning and deep learning models
- Deploying predictions via a web interface

---

## 📊 Project Pipeline

### 🔍 1. Exploratory Data Analysis (EDA)
- Understand customer behavior before, during, and after holidays
- Visualize the effects of promotions, store types, and competition
- Analyze seasonal trends (Christmas, Easter, etc.)
- Handle missing values, outliers, and visualize correlations

### 🔧 2. Data Preprocessing
- Feature engineering from datetime (e.g., holidays, weekends, month start/mid/end)
- Scaling and encoding for model readiness

### 🤖 3. Model Building
- **Machine Learning**: Random Forest Regressor using Scikit-learn pipelines
- **Loss Function**: Custom-selected and explained
- **Deep Learning**: LSTM model with TensorFlow for time series forecasting

### 🔁 4. Model Evaluation
- Feature importance
- Confidence interval analysis
- Visualization of residuals and predictions

### 🧠 5. Model Serialization & MLOps
- Model saved with timestamps for versioning
- MLFlow for model tracking and reproducibility
- DVC for dataset versioning

### 🌐 6. Web App Deployment
- Built with **Flask**
- Allows input of:
  - Store ID
  - CSV Upload (with Date, Promo, Holiday, etc.)
- Returns predicted sales and customer count
- Export results as CSV



