# London-Housing-Data-Analysis-Python-Project-1995-2020-
This project performs detailed exploratory data analysis (EDA) on the London Housing Dataset, which contains monthly housing and crime statistics for London from 1995 to 2020.

📂 Dataset Features

The dataset includes:

📅 Date (Monthly)

📍 Area / Region Name

🏡 Average House Price

🏷 Area Code

🏘 Houses Sold

🚔 Number of Crimes

Total Rows: 13,549
Columns: 6

🔧 Technologies Used

Python

Pandas

NumPy

Matplotlib

Seaborn

🧠 Project Tasks & Analysis Performed
✔ 1. Data Loading & Inspection

Loaded CSV file using Pandas

Checked shape, info, datatypes, and null values

✔ 2. Data Cleaning

Identified missing values (houses_sold, no_of_crimes)

Visualized null value distribution using heatmap

Converted date column to datetime format

✔ 3. Feature Engineering

Created Year and Month columns

Inserted Month column at position 2

Removed unnecessary columns when needed

✔ 4. Analysis & Insights

Extracted all records where no_of_crimes == 0

Calculated:

Maximum & minimum average price per year for England

Maximum crimes recorded per area

Count of records for each area where average_price < 100000

✔ 5. Regional Crime & Price Study

Grouped data by area

Identified high-crime and low-crime zones

Compared historical home affordability

📊 Output Highlights

104 months recorded zero crimes in some areas

Westminster recorded maximum crime count (7461)

Some regions had over 100 records with house prices below £100,000

📁 Project Files

London House Dataset.csv

Day 6 Project.ipynb

PDF Export of analysis

Visualization output images

🚀 How to Run This Project
pip install pandas matplotlib seaborn

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("london house dataset.csv")


Run the remaining code blocks to reproduce analysis and visualizations.
