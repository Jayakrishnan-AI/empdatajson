
import pandas as pd

# Load JSON file
df = pd.read_json("employeedata.json")

# Extract employees list
df = pd.json_normalize(df['employees'])

# Show data
print(df.head(10))

print(df.info())
print(df.describe())

# Average salary
print("Average Salary:", df['SALARY'].mean())

# Highest salary
print("Max Salary:", df['SALARY'].max())

# Employees per department
print(df['DEPARTMENT_ID'].value_counts())

#Histogram-Salary Distribution
import matplotlib.pyplot as plt

plt.hist(df['SALARY'], bins=10)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Count")
plt.show()

#Bar Chart-Employees per Department
dept_counts = df['DEPARTMENT_ID'].value_counts()

dept_counts.plot(kind='bar')
plt.title("Employees per Department")
plt.xlabel("Department ID")
plt.ylabel("Number of Employees")
plt.show()


#Box Plot-Salary by Department
import seaborn as sns

sns.boxplot(x='DEPARTMENT_ID', y='SALARY', data=df)
plt.title("Salary by Department")
plt.show()

#Top Five Highest Pid Employees
top5 = df.sort_values(by='SALARY', ascending=False).head(5)

plt.bar(top5['FIRST_NAME'], top5['SALARY'])
plt.title("Top 5 Salaries")
plt.show()

#Hiring Trend (Year-wise)
df['HIRE_DATE'] = pd.to_datetime(df['HIRE_DATE'])

df['YEAR'] = df['HIRE_DATE'].dt.year

df['YEAR'].value_counts().sort_index().plot(kind='line')
plt.title("Hiring Trend Over Years")
plt.xlabel("Year")
plt.ylabel("Employees Hired")
plt.show()

#Salary Category
df['Salary_Level'] = df['SALARY'].apply(lambda x: 'High' if x > 10000 else 'Low')

#Pie Chart Salary Level
df['Salary_Level'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Salary Category")
plt.show()

#Highest paid employee per department
df.loc[df.groupby('DEPARTMENT_ID')['SALARY'].idxmax()]