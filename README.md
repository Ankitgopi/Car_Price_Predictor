# 🚗 Car Price Predictor  

This project is an end-to-end machine learning application that predicts the resale value of used cars using Quikr data. It demonstrates the complete ML pipeline from **data preprocessing** to **model deployment** via a Flask web app.  

## 🔹 Project Overview  
- **Data Source:** Quikr used car listings  
- **Notebook (Quikr Analysis.ipynb):**  
  - Cleaned and preprocessed raw data (removed duplicates, handled missing values, standardized features)  
  - Performed exploratory data analysis (EDA) and feature engineering  
  - Trained a **Linear Regression** model to estimate car prices  
- **Flask Application (application.py):**  
  - Loads the trained model (`LinearRegressionModel.pkl`)  
  - Provides a web interface for users to input car details (company, model, year, kilometers driven, fuel type)  
  - Returns the **predicted selling price** instantly  

## 🔹 Tech Stack  
- **Python**, **Pandas**, **NumPy**, **Scikit-learn**  
- **Flask** for backend deployment  
- **HTML/CSS** for frontend interface

## 🖼️ Project Demo / Screenshots

#### Here’s a glimpse of the Car Price Predictor web app interface:
   
![App Screenshot](https://github.com/Ankitgopi/Car_Price_Predictor/blob/master/homepage_.png)

![App Screenshot](https://github.com/Ankitgopi/Car_Price_Predictor/blob/master/prediction_.png)




