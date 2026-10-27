"""
AI Training & Learner Performance Analytics System
----------------------------------------------------
A beginner-friendly script that:
1. Loads learner marks from a CSV file using pandas.
2. Calculates each learner's average mark and assigns a grade.
3. Finds the highest- and lowest-scoring learners.
4. Calculates subject-wise average marks across all learners.
5. Draws two bar charts: per-learner averages, and per-subject averages.
6. Writes a plain-text summary report with all the key findings.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

# ----------------------------------------------------------------------
# Step 1: Load the data
# pandas reads the CSV file into a DataFrame (a table-like structure, similar to Excel).
# ----------------------------------------------------------------------
data_path = os.path.join("data", "students.csv")
df = pd.read_csv(data_path)

print("Learner marks loaded:")
print(df)
print()

# ----------------------------------------------------------------------
# Step 2: Calculate each learner's average mark
# The subject columns are everything except "Name".
# ----------------------------------------------------------------------
subject_columns = ["Math", "Science", "English"]
df["Average"] = df[subject_columns].mean(axis=1)

# ----------------------------------------------------------------------
# Step 3: Assign a grade category to each learner based on their average.
#
# Grade boundaries used (editable here if your institution uses different ones):
#   90 and above  -> "A"
#   75 to 89.99   -> "B"
#   60 to 74.99   -> "C"
#   40 to 59.99   -> "D"
#   below 40      -> "F"
# ----------------------------------------------------------------------
GRADE_BOUNDARIES = [
    (90, "A"),
    (75, "B"),
    (60, "C"),
    (40, "D"),
    (0, "F"),
]


def assign_grade(average_mark):
    """Return the grade letter for a given average mark, using GRADE_BOUNDARIES."""
    for minimum_score, grade in GRADE_BOUNDARIES:
        if average_mark >= minimum_score:
            return grade
    return "F"  # fallback, should not normally be reached


df["Grade"] = df["Average"].apply(assign_grade)

print("Marks with each learner's average and grade:")
print(df)
print()

# ----------------------------------------------------------------------
# Step 4: Find the highest- and lowest-scoring learners
# ----------------------------------------------------------------------
top_index = df["Average"].idxmax()
bottom_index = df["Average"].idxmin()
top_learner = df.loc[top_index]
bottom_learner = df.loc[bottom_index]

print(f"Highest-scoring learner: {top_learner['Name']} "
      f"(Average: {top_learner['Average']:.2f}, Grade: {top_learner['Grade']})")
print(f"Lowest-scoring learner: {bottom_learner['Name']} "
      f"(Average: {bottom_learner['Average']:.2f}, Grade: {bottom_learner['Grade']})")
print()

# ----------------------------------------------------------------------
# Step 5: Class-wide and subject-wise statistics
# ----------------------------------------------------------------------
class_average = df["Average"].mean()
subject_averages = df[subject_columns].mean()  # one average per subject column
grade_distribution = df["Grade"].value_counts().sort_index()

print(f"Class average (all learners): {class_average:.2f}")
print("\nSubject-wise averages:")
print(subject_averages)
print("\nGrade distribution:")
print(grade_distribution)

# ----------------------------------------------------------------------
# Step 6: Make sure the output folder exists for charts and reports
# ----------------------------------------------------------------------
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# ----------------------------------------------------------------------
# Step 7: Chart 1 - Average marks per learner (existing chart, unchanged)
# ----------------------------------------------------------------------
plt.figure(figsize=(8, 5))
plt.bar(df["Name"], df["Average"], color="skyblue")
plt.xlabel("Learner")
plt.ylabel("Average Marks")
plt.title("Average Marks per Learner")
plt.ylim(0, 100)
plt.tight_layout()
learner_chart_path = os.path.join(output_dir, "average_marks_chart.png")
plt.savefig(learner_chart_path)
plt.close()
print(f"\nLearner average chart saved to: {learner_chart_path}")

# ----------------------------------------------------------------------
# Step 8: Chart 2 - Average marks per subject (new)
# ----------------------------------------------------------------------
plt.figure(figsize=(8, 5))
plt.bar(subject_averages.index, subject_averages.values, color="lightgreen")
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.title("Average Marks per Subject")
plt.ylim(0, 100)
plt.tight_layout()
subject_chart_path = os.path.join(output_dir, "subject_average_chart.png")
plt.savefig(subject_chart_path)
plt.close()
print(f"Subject-wise average chart saved to: {subject_chart_path}")

# ----------------------------------------------------------------------
# Step 9: Write a plain-text summary report
# ----------------------------------------------------------------------
report_path = os.path.join(output_dir, "summary_report.txt")
with open(report_path, "w", encoding="utf-8") as report_file:
    report_file.write("AI Training & Learner Performance Analytics - Summary Report\n")
    report_file.write("=" * 60 + "\n\n")

    report_file.write(f"Number of learners analysed: {len(df)}\n")
    report_file.write(f"Class average (all learners): {class_average:.2f}\n\n")

    report_file.write("Highest-scoring learner:\n")
    report_file.write(f"  {top_learner['Name']} - Average: {top_learner['Average']:.2f}, "
                       f"Grade: {top_learner['Grade']}\n\n")

    report_file.write("Lowest-scoring learner:\n")
    report_file.write(f"  {bottom_learner['Name']} - Average: {bottom_learner['Average']:.2f}, "
                       f"Grade: {bottom_learner['Grade']}\n\n")

    report_file.write("Subject-wise averages:\n")
    for subject, average_mark in subject_averages.items():
        report_file.write(f"  {subject}: {average_mark:.2f}\n")
    report_file.write("\n")

    report_file.write("Grade distribution:\n")
    for grade, count in grade_distribution.items():
        report_file.write(f"  {grade}: {count} learner(s)\n")

print(f"Summary report saved to: {report_path}")

# Uncomment the line below if you want the charts to pop up in windows too:
# plt.show()
