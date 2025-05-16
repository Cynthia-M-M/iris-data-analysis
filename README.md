🌸 Iris Dataset Analysis Project
📋 Project Overview
This project involves exploring and visualizing the famous Iris dataset using Python. The goal is to perform basic data analysis and produce visual insights about the dataset in a way that's friendly for beginners learning data science.

🔧 Technologies Used
Python 3.x

pandas

matplotlib

seaborn

scikit-learn (for loading the dataset)

📁 How to Run the Project
Make sure you have Python installed.

Install the required libraries:

bash
Copy
Edit
pip install pandas matplotlib seaborn scikit-learn
Save the script as iris_analysis.py and run it:

bash
Copy
Edit
python iris_analysis.py
Charts will be displayed on screen and saved in your current project directory as:

line_chart.png

bar_chart.png

histogram.png

scatter_plot.png

📊 Dataset Description
The Iris dataset contains 150 samples of iris flowers, each described by four features:

Sepal Length (cm)

Sepal Width (cm)

Petal Length (cm)

Petal Width (cm)

Target (species encoded as 0, 1, or 2)

🔍 Analysis Steps
✅ 1. Preview of Dataset
First 5 Rows:

scss
Copy
Edit
   sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)  target
0                5.1               3.5                1.4               0.2       0
1                4.9               3.0                1.4               0.2       0
2                4.7               3.2                1.3               0.2       0
3                4.6               3.1                1.5               0.2       0
4                5.0               3.6                1.4               0.2       0
✅ 2. Data Types
scss
Copy
Edit
sepal length (cm)    float64  
sepal width (cm)     float64  
petal length (cm)    float64  
petal width (cm)     float64  
target                 int64  
✅ 3. Missing Values
scss
Copy
Edit
sepal length (cm)    0  
sepal width (cm)     0  
petal length (cm)    0  
petal width (cm)     0  
target               0  
✅ There are no missing values in the dataset.

✅ 4. Statistical Summary
matlab
Copy
Edit
       sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)      target
count         150.000000        150.000000         150.000000        150.000000  150.000000
mean            5.843333          3.057333           3.758000          1.199333    1.000000
std             0.828066          0.435866           1.765298          0.762238    0.819232
min             4.300000          2.000000           1.000000          0.100000    0.000000
25%             5.100000          2.800000           1.600000          0.300000    0.000000
50%             5.800000          3.000000           4.350000          1.300000    1.000000
75%             6.400000          3.300000           5.100000          1.800000    2.000000
max             7.900000          4.400000           6.900000          2.500000    2.000000
✅ 5. Mean by Species
Grouped by target:

scss
Copy
Edit
        sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
target                                                                         
0                   5.006             3.428              1.462             0.246
1                   5.936             2.770              4.260             1.326
2                   6.588             2.974              5.552             2.026
📌 Key Observations
Setosa species tend to have the smallest petal lengths and widths.

Virginica species have the largest values for both petal length and width.

Sepal dimensions vary but not as dramatically as petal features.

📷 Visualizations
The following visualizations were created and saved as PNG images:

📈 Line Chart — Sepal and Petal Length over sample index

📊 Bar Chart — Average Petal Length per Species

📉 Histogram — Sepal Width Distribution

🔴 Scatter Plot — Sepal Length vs Petal Length, colored by species

🙋🏽‍♀️ Made By
This analysis was completed by Cynthia as part of a learning project to explore foundational data analysis using Python 🐍.

