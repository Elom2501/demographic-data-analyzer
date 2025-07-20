📊 Demographic Data Analyzer
Project Description

This project is part of the freeCodeCamp Data Analysis with Python Certification.

It involves analyzing demographic data from the 1994 US Census (Adult Data Set) using Python and Pandas.
The goal is to extract insightful statistics about education, income, race, and occupation.
Challenge Objectives

As part of the freeCodeCamp Data Analysis certification, the project requires you to:

    Manipulate and filter large datasets with Pandas

    Perform statistical calculations

    Understand data grouping and aggregation

    Write clean, testable Python code

Main Features

    Count of individuals by race

    Average age of men

    Percentage of people with a Bachelor's degree

    Income analysis for people with/without advanced education

    Minimum working hours and income correlation

    Country-wise income analysis

    Most popular occupations among high-income earners in India

Usage

Run the analysis:

python main.py

Testing

This project includes unit tests to verify your code:

pytest test_module.py

Requirements

    Python 3.x

    pandas

    pytest

Dataset

    Source: UCI Machine Learning Repository - Adult Data Set

    Purpose: Originally used to predict whether an individual earns more than $50K/year based on census data.

Folder Structure

demographic-data-analyzer/
│
├── demographic_data_analyzer.py   # Main analysis functions
├── main.py                         # Script to run the analysis
├── test_module.py                  # Unit tests (freeCodeCamp test cases)
├── adult.data.csv                  # Dataset (optional: use link if file is too large)
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation

License

This is an educational project developed for freeCodeCamp learning purposes.
