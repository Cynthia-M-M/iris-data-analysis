# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Task 1: Load and Explore the Dataset
try:
    # Load iris dataset from sklearn
    iris_data = load_iris(as_frame=True)
    df = iris_data.frame

    # Display first few rows
    print("First 5 rows of the dataset:")
    print(df.head())

    # Check data types and missing values
    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    # No missing values, so no cleaning needed
except FileNotFoundError:
    print("Dataset file not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# Task 2: Basic Data Analysis
print("\nStatistical Summary:")
print(df.describe())

# Group by species and compute mean
grouped = df.groupby('target').mean()
print("\nMean of features grouped by species:")
print(grouped)

# Map target numbers to actual species names
df['species'] = df['target'].map(dict(zip(range(3), iris_data.target_names)))

# Insights
print("\nObservations:")
print("- Setosa tends to have smaller petal lengths and widths.")
print("- Virginica has the highest mean values for petal length and width.")

# Task 3: Data Visualization

# Line Chart (simulate time trend using index)
plt.figure(figsize=(8, 5))
plt.plot(df.index, df['sepal length (cm)'], label='Sepal Length')
plt.plot(df.index, df['petal length (cm)'], label='Petal Length')
plt.title("Sepal and Petal Length Over Index")
plt.xlabel("Index")
plt.ylabel("Length (cm)")
plt.legend()
plt.grid(True)
plt.savefig("line_chart.png")
plt.show()

# Bar Chart - Average petal length per species
plt.figure(figsize=(6, 4))
sns.barplot(data=df, x='species', y='petal length (cm)', hue='species', palette="Set2", legend=False)
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.savefig("bar_chart.png")
plt.show()

# Histogram of sepal width
plt.figure(figsize=(6, 4))
plt.hist(df['sepal width (cm)'], bins=10, color='skyblue', edgecolor='black')
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.savefig("histogram.png")
plt.show()

# Scatter Plot: Sepal vs Petal Length
plt.figure(figsize=(6, 4))
sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species', palette="Set1")
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.savefig("scatter_plot.png")
plt.show()
