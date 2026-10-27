"""
Student Marks Analyser
-----------------------
A beginner-friendly script that:
1. Loads student marks from a CSV file using pandas.
2. Calculates each student's average mark.
3. Finds the highest-scoring student.
4. Draws a bar chart of average marks using matplotlib.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

# Step 1: Load the data
# pandas reads the CSV file into a DataFrame (a table-like structure, similar to Excel).
data_path = os.path.join("data", "students.csv")
df = pd.read_csv(data_path)

print("Student marks loaded:")
print(df)
print()

# Step 2: Calculate each student's average mark
# The subject columns are everything except "Name".
subject_columns = ["Math", "Science", "English"]
df["Average"] = df[subject_columns].mean(axis=1)

print("Marks with each student's average:")
print(df)
print()

# Step 3: Find the highest-scoring student
top_student_index = df["Average"].idxmax()
top_student = df.loc[top_student_index]

print(f"Highest-scoring student: {top_student['Name']} "
      f"(Average: {top_student['Average']:.2f})")
print()

# Also show the overall class average, just for extra insight.
class_average = df["Average"].mean()
print(f"Class average (all students): {class_average:.2f}")

# Step 4: Create a bar chart of average marks per student
plt.figure(figsize=(8, 5))
plt.bar(df["Name"], df["Average"], color="skyblue")
plt.xlabel("Student")
plt.ylabel("Average Marks")
plt.title("Average Marks per Student")
plt.ylim(0, 100)
plt.tight_layout()

# Step 5: Save the chart as an image instead of (or in addition to) showing it
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "average_marks_chart.png")
plt.savefig(output_path)
print(f"\nBar chart saved to: {output_path}")

# Uncomment the line below if you want the chart to pop up in a window too:
# plt.show()
