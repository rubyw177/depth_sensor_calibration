# Sensor Calibration with Linear Regression

## Overview
This project implements a **sensor calibration** method using **linear regression** to correlate sensor readings with actual measurements. The script reads sensor data from a CSV file, applies a regression model to find the best fit, and visualizes the results.

## Features
- **Reads sensor data** from a CSV file.
- **Applies linear regression** to establish a correlation between sensor values and actual values.
- **Splits data into training and testing sets** for model evaluation.
- **Generates performance metrics** such as the regression equation.
- **Plots visualizations** to illustrate sensor accuracy and model performance.

## Dependencies
Ensure you have the following Python libraries installed:
```bash
pip install numpy pandas matplotlib scikit-learn
```

## Usage
### 1. Prepare Sensor Data
The dataset should be in **CSV format**, with two columns:
- **First column**: Sensor readings
- **Second column**: Actual measured values (e.g., in cm)

### 2. Run the Calibration Script
```bash
python sensor_cal.py
```
This script:
1. **Loads the dataset** from `Book1.csv`.
2. **Splits data** into training (70%) and testing (30%).
3. **Trains a linear regression model** to predict actual values from sensor readings.
4. **Evaluates model performance**.
5. **Plots results** for both training and test sets.
6. **Saves the output visualization** as `grafik.png`.

### 3. Output Example
#### Regression Equation:
```
y = b0 + (b1 * x)
```
Where:
- **b0** = Intercept
- **b1** = Slope coefficient

## Visualizations
- **Training Set**: Shows the linear fit between sensor and actual values.
- **Test Set**: Compares predictions with actual test values.
- **Overall Data Fit**: Displays the complete dataset with regression predictions.
