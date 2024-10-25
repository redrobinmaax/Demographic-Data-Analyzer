#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

def demographic_data_analyzer():
    # Read the dataset
    df = pd.read_csv('adult.data.csv')
    
    # How many people of each race are represented in this dataset?
    race_count = df['race'].value_counts()
    
    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
    
    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)
    
    # Advanced education: Bachelors, Masters, or Doctorate
    advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    
    # What percentage of people with advanced education make more than 50K?
    higher_education_rich = round((df[advanced_education]['salary'] == '>50K').mean() * 100, 1)
    
    # What percentage of people without advanced education make more than 50K?
    lower_education_rich = round((df[~advanced_education]['salary'] == '>50K').mean() * 100, 1)
    
    # What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()
    
    # What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((min_workers['salary'] == '>50K').mean() * 100, 1)
    
    # What country has the highest percentage of people that earn >50K?
    country_rich_percentage = (df[df['salary'] == '>50K']['native-country'].value_counts() /
                               df['native-country'].value_counts() * 100).idxmax()
    highest_earning_country_percentage = round((df[df['salary'] == '>50K']['native-country'].value_counts() /
                                                df['native-country'].value_counts() * 100).max(), 1)
    
    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]
    
    # Return the answers in a dictionary
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': country_rich_percentage,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

