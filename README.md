## 🏡 House Price Prediction 📊

### 📜 Project Overview

This project aims to predict house prices based on various property and neighborhood features. By analyzing a large residential dataset, we explore key factors driving house prices and train predictive models to help estimate home values accurately.

### 🎯 Objectives

* Perform data exploration and cleaning
* Identify price-driving features
* Develop and evaluate predictive models
* Optimize model performance using hyperparameter tuning

### 🧠 Key Steps

1. **Data Exploration & Cleaning**:

   * Removed irrelevant columns (`date`, `country`, `street`, `city`)
   * Checked and handled missing values and outliers
   * Performed correlation analysis to identify important features

2. **Feature Engineering**:

   * Encoded categorical data using one-hot encoding
   * Derived new features like `age_of_property`

3. **Model Training & Tuning**:

   * Applied models like Linear Regression, Random Forest, XGBoost
   * Tuned hyperparameters with GridSearchCV and RandomizedSearchCV

4. **Evaluation & Analysis**:

   * Assessed models using RMSE, R²
   * Visualized feature importances and residuals

### 📈 Best Model Performance

| Model             | RMSE     | R²      |
| ----------------- | -------  | ------- |
| Linear Regression | 12958.47 | 1.00    |
| RandomForest      | 48049.82 | 0.98    |
| XGBoost           | 37102.19 | 0.99    |

🏆 **Linear Regression** performed the best, showing the lowest RMSE and highest R² score.

### 🧑‍💻 Usage Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/yash-vasani-01/CSI-25_project
   ```
2. Install requirements:

   ```bash
   pip install -r requirements.txt
   ```
3. Run the Jupyter Notebook:

   ```bash
   jupyter notebook House_Price_Prediction.ipynb
   ```

### 🙏 Acknowledgements

Special thanks to my mentors and Celebal Technologies for this learning opportunity!
