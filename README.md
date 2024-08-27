# Car Price Detector

This project is a Car Price Detector that predicts the price of a car based on various features such as the car's name, company, year, fuel type, and kilometers driven. The model was built using Python and machine learning techniques.

## Table of Contents
- Overview
- Dataset
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Model Building
- Results
- Dependencies
- Conclusion

## Overview
This project involves predicting the price of used cars using machine learning algorithms. The data was cleaned and processed before being used to train a linear regression model, which was then tested for accuracy.

## Dataset
The dataset was obtained from Quikr, containing details about various cars, including:
- Name
- Company
- Year of Manufacture
- Price
- Kilometers Driven
- Fuel Type

## Data Cleaning
Several preprocessing steps were performed to clean the data:
- Removed non-numeric year values.
- Converted the year and price columns to integer types.
- Removed rows with missing values in critical columns.
- Extracted relevant words from the car name for better modeling.

## Exploratory Data Analysis (EDA)
Basic exploratory data analysis was conducted to understand the distribution and correlation of the features. Outliers in the price column were also removed to improve model performance.

## Model Building
A linear regression model was built to predict car prices based on the following features:
- Car name
- Company
- Fuel type
- Year
- Kilometers driven

The model was evaluated using the R-squared score. Multiple iterations were run with different random states to find the best-performing model.


## Results
The linear regression model achieved an R-squared score of `84.57%` with the best random state.

## Dependencies
- pandas
- numpy
- scikit-learn

## Conclusion
The Car Price Detector successfully predicts the price of used cars based on multiple features. Future improvements could involve using more advanced models or incorporating additional features like car condition or market trends.
