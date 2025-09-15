# 📊 Data Portfolio  

Welcome to my data portfolio!  
This repository showcases my journey from **Data Analyst → Data Scientist → AI Product Developer**, with hands-on projects in **Data Analytics, Machine Learning, and AI-powered solutions**.  

---

## 🚀 Project 1: Netflix Data Analysis (Day 1)  

**Goal**: Explore and clean the Netflix dataset to understand recent content trends and build reusable data workflows.  

### 🔑 Key Insights
- Total records analyzed: **8,807**
- Filtered to movies from **2015–2021 → 4,017 rows**
- **Top Genres (2015+)**:
  1. International Movies (1845)  
  2. Dramas (1564)  
  3. Comedies (948)  
  4. Documentaries (730)  
  5. Independent Movies (548)  

### 📂 Outputs
- **Cleaned dataset** → [`outputs/netflix_movies_2015plus_clean.csv`](outputs/netflix_movies_2015plus_clean.csv)  
- **Top genres visualization** → [`outputs/top_genres_movies_2015plus.png`](outputs/top_genres_movies_2015plus.png)  
- **Summary report** → [`outputs/day1_summary.txt`](outputs/day1_summary.txt)  

### 🛠️ Tools & Tech
- Python → Pandas, Numpy, Matplotlib  
- Data Cleaning & Transformation  
- Exploratory Data Analysis (EDA)  
- Git & GitHub  

---

## 📌 Roadmap
This portfolio will grow with:
- Advanced **Data Analytics projects**
- **Machine Learning models**
- **AI-driven product prototypes**  

Follow this repo ⭐ to see new projects as I build my way towards **AI Product Development**.

# 📊 Day 1 — Data Analysis Basics (Practice)

This project contains my first practice script for learning **pandas** and basic data analysis.

---

## ✅ What I Practiced
- **Importing pandas** (`import pandas as pd`)
- **Creating user-defined dataset** (dictionary → DataFrame)
- **Inspecting data**
  - `.shape` → Get number of rows and columns
  - `.head(n)` → Preview first n rows
- **Filtering data**
  - By column values (`df[df["Author"]=="Moses"]`)
- **Finding range**
  - `.min()` and `.max()` for column values

---

## 📂 File Location
`src/user-defined_data.py`

---

## 🖥 Example Output
Sample console output when running the script:

---DATA FRAME---
     Title Released Author  year
0  Genesis    BC 45  Moses  2021
1   Exodus    BC 48  Moses  2021
3     John    AD 49  Moses  2023

---SHAPE---
 (4, 4)
---FIRST 3 HEAD VALUES(3)---
      Title Released Author  year
0  Genesis    BC 45  Moses  2021
1   Exodus    BC 48  Moses  2021
2     Luke    AD 45   Luke  2024

---Filter AUTHOR---

     Title Released Author  year
0  Genesis    BC 45  Moses  2021
1   Exodus    BC 48  Moses  2021
3     John    AD 49  Moses  2023

---Filter YEAR---

     Title Released Author  year
0  Genesis    BC 45  Moses  2021
1   Exodus    BC 48  Moses  2021

---EARLIEST RELEASE YEAR---

AD 45

---LATEST RELEASE YEAR---

BC 48

---

## 🎯 Learning Goal
This script helps me:
- Understand **DataFrame basics**.
- Practice **filtering & summarizing data**.
- Build confidence for larger real-world datasets (e.g., Netflix dataset in Day 1 project).

---




