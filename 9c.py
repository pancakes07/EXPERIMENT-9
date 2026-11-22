import pandas as pd
import matplotlib.pyplot as plt

data = { 
        "Name" : ["Rahul", "Aman", "Priya", "Sneha", "Karan", "Neha", "Rohan"],
        "Salary" : [45000, 60000, 35000, 90000, 55000, 70000, 85000],
        "Score" : [85,92,78,95,80,88,98]
        }

df = pd.DataFrame(data)

print("Student Dataset:")
print(df)


#1.Bar Chart - Employee Salary
plt.figure()
plt.bar(df["Name"], df["Salary"])
plt.xlabel("Emplyee Name")
plt.ylabel("Salary")
plt.title("Employee Marks - Bar Chart")
plt.show()

#2.Line Chart - Employee Salary
plt.figure()
plt.plot(df["Name"], df["Salary"], marker = "o")
plt.xlabel("Score")
plt.ylabel("Salary")
plt.title("Employee Marks - Line Chart")
plt.show()

#3.Pie Chart - Salary
plt.figure()
plt.pie(
    df["Salary"],
    labels=df["Name"],
    autopct="%1.1f%%"
)
plt.title("Employee Salary - Pie Chart")
plt.show()

#4. Scatter Plot - Salary vs Score
plt.figure()
plt.scatter(df["Score"], df["Salary"])
plt.xlabel("Salary")
plt.ylabel("Score")
plt.title("Salary vs Score - Scatter Plot")
plt.show()


#5. Histogram - Distribution of Salary
plt.figure()
plt.hist(df["Salary"],bins = 5)
plt.xlabel("Salary")
plt.ylabel("Number of Employee")
plt.title("Salary Distribution")
plt.show()
