# Student Marks Analyser

A beginner-friendly Python project that analyses synthetic student marks using **pandas** and **matplotlib**.

## What it does

1. Loads student marks (Math, Science, English) from `data/students.csv`.
2. Calculates each student's average mark.
3. Identifies the highest-scoring student and the class average.
4. Generates a bar chart comparing students' average marks, saved to `output/average_marks_chart.png`.

## Project structure

```
student-marks-analysis/
├── data/
│   └── students.csv              # synthetic dataset
├── analyse_marks.py               # main script
├── output/
│   └── average_marks_chart.png    # generated chart (created after running the script)
└── README.md
```

## Setup

This project uses a virtual environment to keep dependencies isolated.

```bash
# 1. Create a virtual environment
python -m venv venv

# 2. Activate it
# On Windows (PowerShell):
venv\Scripts\Activate.ps1
# On Windows (cmd.exe):
venv\Scripts\activate.bat

# 3. Install dependencies
python -m pip install pandas matplotlib
```

## Running the script

```bash
python analyse_marks.py
```

This prints the marks table, the averages, the top student, and the class average to the terminal, and saves a bar chart image to `output/average_marks_chart.png`.

## Viewing the chart

Open `output/average_marks_chart.png` in any image viewer, or in VS Code/File Explorer by double-clicking it.
