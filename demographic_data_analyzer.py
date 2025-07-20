import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # 1. Number of each race represented in the dataset
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage of people with a Bachelor's degree
    total_people = df.shape[0]
    bachelors_count = df[df['education'] == 'Bachelors'].shape[0]
    percentage_bachelors = round((bachelors_count / total_people) * 100, 1)

    # 4. Percentage of people with advanced education earning >50K
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education

    higher_education_rich = round((df[higher_education & (df['salary'] == '>50K')].shape[0] / df[higher_education].shape[0]) * 100, 1)
    lower_education_rich = round((df[lower_education & (df['salary'] == '>50K')].shape[0] / df[lower_education].shape[0]) * 100, 1)

    # 5. Minimum number of hours worked per week
    min_work_hours = df['hours-per-week'].min()

    # 6. Percentage of rich people among those who work the minimum hours
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_min_workers = num_min_workers[num_min_workers['salary'] == '>50K'].shape[0]

    if num_min_workers.shape[0] == 0:
        rich_percentage = 0.0
    else:
        rich_percentage = round((rich_min_workers / num_min_workers.shape[0]) * 100, 1)

    # 7. Country with the highest percentage of rich (>50K)
    country_counts = df['native-country'].value_counts()
    rich_country_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    rich_country_percentage = (rich_country_counts / country_counts) * 100

    highest_earning_country = rich_country_percentage.idxmax()
    highest_earning_country_percentage = round(rich_country_percentage.max(), 1)

    # 8. Most popular occupation for rich people in India
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE
    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
