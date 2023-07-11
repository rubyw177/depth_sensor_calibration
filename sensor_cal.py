import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Book1.csv')
X = dataset.iloc[:, 0].values.reshape(-1,1) # Supposed to be Sensor Value
y = dataset.iloc[:, 1].values # Supposed to be Actual Value in cm

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 69)

# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test Results
y_pred = regressor.predict(X_test)

# Add superscript
superscript = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
k = "2".translate(superscript)

# Visualising the Results of the Training Test
plt.scatter(X_train, y_train, color = "red")
plt.plot(X_train, regressor.predict(X_train), color = "blue")
plt.title("Training Set")
plt.title("Actual Value vs Sensor Value")
plt.xlabel("Sensor Value")
plt.ylabel("Actual Value (cm)")
plt.show()

# Visualising the Results of the Test Test
plt.scatter(X_test, y_test, color = "red")
plt.plot(X_train, regressor.predict(X_train), color = "blue")
plt.title("Test Set")
plt.title("Actual Value vs Sensor Value")
plt.xlabel("Sensor Value")
plt.ylabel("Actual Value (cm)")
plt.show()

# Visualising the Results of the data
plt.scatter(X, y, color = "black")
plt.plot(X, regressor.predict(X), color = "yellow")
plt.title("Actual Value vs Sensor Value")
plt.xlabel("Sensor Value")
plt.ylabel("Actual Value (cm)")
plt.savefig("grafik.png", dpi=300)
plt.show()

# Print b0, b1 and R squared
b1 = regressor.coef_
b0 = regressor.intercept_
r_sq = regressor.score(X, y)

print("y = %f + %fx" %(b0, b1))
print("R{} = {}%".format(k, r_sq*100))
