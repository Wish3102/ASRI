# Velocity Analysis and Linear Regression with Fireball Data

This Python project performs data analysis and visualization on fireball velocity data. The code calculates correlations between different velocity components and the overall velocity, visualizes the data with scatter plots and correlation heatmaps, and computes linear regression models to analyze trends in the data.

## Project Overview

The project analyzes fireball velocity components in the dataset and explores relationships between these components. The following analyses are performed:

- **Correlation Analysis**: The correlation between various velocity components (`vx`, `vy`, `vz`) and the overall velocity (`Velocity (km/s)`) is computed and visualized with a heatmap.
- **Linear Regression**: Linear regression models are applied to each of the velocity components (`vx`, `vy`, `vz`) to calculate the gradient (slope), indicating the relationship between each component and the overall velocity.
- **Visualization**: Scatter plots with best-fit lines and heatmaps are generated to visually interpret the relationships and correlations in the data.

## Features

- **Data Correlation Calculation**: The code calculates the Pearson correlation coefficients between the target velocity column and other components (`vx`, `vy`, `vz`).
- **Heatmap Visualization**: Correlation matrices and individual correlations are displayed as heatmaps using `seaborn`.
- **Scatter Plot and Regression Line**: Scatter plots with linear regression lines are generated to visually analyze the relationship between each velocity component and the target velocity.
- **Linear Regression Analysis**: The slope (gradient) of the regression lines is calculated for each velocity component using `scikit-learn`'s `LinearRegression`.

## Dependencies

- **Python 3.x**
- **Pandas**: For data manipulation and reading CSV files.
- **NumPy**: For numerical operations and regression analysis.
- **Matplotlib**: For plotting graphs and visualizations.
- **Seaborn**: For advanced visualization (heatmaps, etc.).
- **Scikit-learn**: For creating and fitting linear regression models.

## Installation

To run this project, clone this repository and install the necessary dependencies using `pip`.

```bash
git clone https://github.com/Wish3102/fireball-velocity-analysis.git
cd fireball-velocity-analysis
pip install -r requirements.txt

