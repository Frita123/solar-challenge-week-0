# solar-challenge-week-0
## Solar Challenge Project

## Overview
This project explores solar energy data from Benin, Sierra Leone, and Togo.
We cleaned the data, analyzed it, and built a Streamlit dashboard to compare solar performance between the countries.

## Step 1: Setup
-Created the GitHub repo solar-challenge-week1.
-Set up a Python virtual environment.
-Added a .gitignore to skip data and venv files.
-Installed all libraries from requirements.txt.
-Used GitHub Actions to check environment setup.

## Step 2: Data Cleaning & EDA
-Made separate branches: eda-benin, eda-sierraleone, eda-togo.
-Cleaned datasets: removed or filled missing values and outliers.
-Saved cleaned files (*_clean.csv).
-Used Pandas, Matplotlib, and Seaborn to create plots and explore data.
-Found that GHI, DNI, DHI are highly related, and humidity lowers solar output.

## Step 3: Country Comparison
-Combined all cleaned datasets.
-Compared solar results using boxplots and summary tables.
-Found Benin had the highest average GHI.
-Used ANOVA tests to confirm differences between countries.

## Step 4: Dashboard
-Built a Streamlit app (app/main.py).
Added:
-Dropdown to select countries
-Interactive Plotly charts
-Tables for top solar readings
-Comparison boxplots
-Saved screenshots in the dashboard_screenshots folder.

The project covered everything from data cleaning to dashboard creation.
It shows how Git, Python, and Streamlit can be used together for solar data analysis.

