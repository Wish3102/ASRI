# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('fireballs.csv')

df

# Choose the column for comparison (replace 'target_column' with your choice)
target_column = 'Velocity (km/s)'

# Calculate correlation with the chosen column
# Pass the Series directly to the corr method
selected_columns = ['Velocity Components (km/s): vx', 'Velocity Components (km/s): vy', 'Velocity Components (km/s): vz']
correlation_series = df[selected_columns].corrwith(df['Velocity (km/s)'])

# Plot the correlation series

plt.figure(figsize=(5, 5))
sns.heatmap(correlation_series.to_frame(), annot=True, cmap='coolwarm')  # Convert to DataFrame for heatmap
plt.xlabel('Velocity (km/s)')
plt.ylabel('Correlation')
plt.title('Correlation of Velocity (km/s) with other component velocities')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()

correlation_matrix = df.corr(numeric_only=True)
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()

coefficients

y_data = df['Velocity (km/s)']
x_data = df['Velocity Components (km/s): vy']
x_data= x_data.dropna()
y_data = y_data.dropna()
x_data = x_data[x_data != 0]
y_data = y_data[y_data != 0]
x_col = 'Velocity Components (km/s): vy'
y_col = 'Velocity (km/s)'
plt.xlabel(x_col)  # Label for x-axis
plt.ylabel(y_col)  # Label for y-axis
plt.title("Scatter Plot of " + x_col + " vs " + y_col)  # Plot title
plt.grid(True)
coefficients = np.polyfit(x_data, y_data, 1) # Use numerical data here
line_of_best_fit = np.polyval(coefficients, x_data)
plt.scatter(x_data, y_data)
plt.plot(x_data, line_of_best_fit, color='red')
plt.show()

#Gradient of Velocity Components (km/s): vz
import numpy as np
from sklearn.linear_model import LinearRegression

# Sample data
x = x_data.values.reshape(-1, 1) # Reshape x_data to a 2D array
y = y_data

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(x, y)

# The slope is the coefficient of the x variable
slope = model.coef_[0]

print(f'Gradient of {x_col[-2:]}:',slope)

y_data = df['Velocity (km/s)']
x_data = df['Velocity Components (km/s): vx']
x_data= x_data.dropna()
y_data = y_data.dropna()
x_data = x_data[x_data != 0]
y_data = y_data[y_data != 0]
x_col = 'Velocity Components (km/s): vx'
y_col = 'Velocity (km/s)'
plt.xlabel(x_col)  # Label for x-axis
plt.ylabel(y_col)  # Label for y-axis
plt.title("Scatter Plot of " + x_col + " vs " + y_col)  # Plot title
plt.grid(True)
coefficients = np.polyfit(x_data, y_data, 1) # Use numerical data here
line_of_best_fit = np.polyval(coefficients, x_data)
plt.scatter(x_data, y_data)
plt.plot(x_data, line_of_best_fit, color='red')
plt.show()

#Gradient of Velocity Components (km/s): vz
import numpy as np
from sklearn.linear_model import LinearRegression

# Sample data
x = x_data.values.reshape(-1, 1) # Reshape x_data to a 2D array
y = y_data

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(x, y)

# The slope is the coefficient of the x variable
slope = model.coef_[0]

print(f'Gradient of {x_col[-2:]}:',slope)

y_data = df['Velocity (km/s)']
x_data = df['Velocity Components (km/s): vz']
x_data= x_data.dropna()
y_data = y_data.dropna()
x_data = x_data[x_data != 0]
y_data = y_data[y_data != 0]
x_col = 'Velocity Components (km/s): vz'
y_col = 'Velocity (km/s)'
plt.xlabel(x_col)  # Label for x-axis
plt.ylabel(y_col)  # Label for y-axis
plt.title("Scatter Plot of " + x_col + " vs " + y_col)  # Plot title
plt.grid(True)
coefficients = np.polyfit(x_data, y_data, 1) # Use numerical data here
line_of_best_fit = np.polyval(coefficients, x_data)
plt.scatter(x_data, y_data)
plt.plot(x_data, line_of_best_fit, color='red')
plt.show()

#Gradient of Velocity Components (km/s): vz
import numpy as np
from sklearn.linear_model import LinearRegression

# Sample data
x = x_data.values.reshape(-1, 1) # Reshape x_data to a 2D array
y = y_data

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(x, y)

# The slope is the coefficient of the x variable
slope = model.coef_[0]

print(f'Gradient of {x_col[-2:]}:',slope)
