#set up
import pandas as pd
from pathlib import Path

# File to Load (Remember to Change These)
school_data_to_load = Path("Resources/schools_complete.csv")
student_data_to_load = Path("Resources/students_complete.csv")

# Read School and Student Data File and store into Pandas DataFrames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset.  
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])
school_data_complete.head()

# Assuming you have a DataFrame 'df' with the necessary data columns

# Total number of unique schools
total_unique_schools = df['school_name'].nunique()

# Total students
total_students = len(df)

# Total budget
total_budget = df['budget'].sum()

# Average math score
average_math_score = df['math_score'].mean()

# Average reading score
average_reading_score = df['reading_score'].mean()

# % passing math
passing_math_percentage = (len(df[df['math_score'] >= 70]) / total_students) * 100

# % passing reading
passing_reading_percentage = (len(df[df['reading_score'] >= 70]) / total_students) * 100

# % overall passing
overall_passing_percentage = (len(df[(df['math_score'] >= 70) & (df['reading_score'] >= 70)]) / total_students) * 100

# Create a DataFrame to store the metrics
district_summary = pd.DataFrame({
    'Total Schools': [total_unique_schools],
    'Total Students': [total_students],
    'Total Budget': [total_budget],
    'Average Math Score': [average_math_score],
    'Average Reading Score': [average_reading_score],
    '% Passing Math': [passing_math_percentage],
    '% Passing Reading': [passing_reading_percentage],
    '% Overall Passing': [overall_passing_percentage]
})

# Display the district summary
print(district_summary)
