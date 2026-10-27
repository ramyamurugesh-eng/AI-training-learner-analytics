# AI Training & Learner Performance Analytics System

A beginner-friendly Python project that analyses synthetic learner marks using **pandas** and **matplotlib**, built up step by step as a learning exercise.

## Features

- Loads learner marks (Math, Science, English) from a CSV file.
- Calculates each learner's **average mark**.
- Assigns a **grade category** (A/B/C/D/F) to each learner based on documented thresholds.
- Identifies the **highest-** and **lowest-scoring learners**.
- Calculates **subject-wise average marks** across all learners.
- Calculates the **grade distribution** (how many learners fall into each grade).
- Generates **two bar charts**:
  - Average marks per learner
  - Average marks per subject
- Writes a **plain-text summary report** with all the key findings.

## Project structure

```
Claude Code Exp/
├── data/
│   └── students.csv                   # synthetic dataset
├── analyse_marks.py                    # main script
├── output/
│   ├── average_marks_chart.png         # chart: average marks per learner
│   ├── subject_average_chart.png       # chart: average marks per subject
│   └── summary_report.txt              # text report with key statistics
├── venv/                               # virtual environment (not committed to git)
└── README.md
```

## Grade categories

Grades are assigned from each learner's average mark using these boundaries (edit `GRADE_BOUNDARIES` in `analyse_marks.py` to change them):

| Average mark | Grade |
|---|---|
| 90 and above | A |
| 75 – 89.99 | B |
| 60 – 74.99 | C |
| 40 – 59.99 | D |
| below 40 | F |

## Setup

This project uses a virtual environment (already created in `venv/`) to keep dependencies isolated from your system Python.

If you're setting this up fresh (e.g., on another machine):

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

If the `venv` folder already exists (as it does in this project), just activate it — no need to reinstall anything.

## Running the script

With the virtual environment already set up, you can run the script directly without activating, using the venv's own Python:

```bash
venv\Scripts\python analyse_marks.py
```

Or, if you've activated the virtual environment first:

```bash
python analyse_marks.py
```

### What happens when you run it

The script prints to the terminal:
- The raw marks table
- The table with each learner's average and grade added
- The highest- and lowest-scoring learners
- The class average
- Subject-wise averages
- The grade distribution

It also creates/updates these files in `output/`:
- `average_marks_chart.png` — bar chart of average marks per learner
- `subject_average_chart.png` — bar chart of average marks per subject
- `summary_report.txt` — plain-text report summarizing all the above

## Viewing the outputs

- Open the `.png` files in `output/` with any image viewer, or double-click them in File Explorer / VS Code.
- Open `output/summary_report.txt` in any text editor to read the summary report.

## Testing your changes

If you edit `data/students.csv` (e.g., add/remove learners or change marks) or change the grade boundaries in `analyse_marks.py`, just re-run the script:

```bash
venv\Scripts\python analyse_marks.py
```

The console output, both charts, and the summary report will all be regenerated from the current data.
