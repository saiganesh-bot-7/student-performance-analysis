# 📊 Student Performance Analysis

A Python-based data analysis project that explores student academic performance using **NumPy, Pandas, Matplotlib, and Seaborn**.

The project analyzes subject marks, calculates student averages, examines attendance and study hours, and generates visualizations to help understand academic performance.

## 🚀 Project Objectives

* Analyze students' marks across multiple subjects.
* Calculate total and average marks.
* Identify the highest-scoring student.
* Compare average performance across subjects.
* Explore the relationship between attendance and academic results.
* Visualize the relationship between study hours and average marks.
* Examine correlations between numerical variables.

## 🛠️ Technologies Used

| Library    | Purpose                                     |
| ---------- | ------------------------------------------- |
| Python     | Core programming language                   |
| NumPy      | Numerical calculations and rounding         |
| Pandas     | Data loading, cleaning checks, and analysis |
| Matplotlib | Data visualization                          |
| Seaborn    | Statistical plots and correlation heatmaps  |

## 📁 Project Structure

```text
Student-Performance-Analysis/
│
├── data/
│   └── students.csv
│
├── outputs/
│   ├── student_analysis.csv
│   ├── subject_averages.png
│   ├── study_vs_marks.png
│   └── correlation_heatmap.png
│
├── main.py
├── README.md
└── requirements.txt
```

*Note: The output files are generated when the program runs successfully. The `requirements.txt` file must be created separately if it does not already exist.*

## 📈 Features

### 1. Dataset Analysis

* Displays the first few rows of the dataset.
* Reports the number of rows and columns.
* Lists column names.
* Generates descriptive statistics.
* Checks for missing values.

### 2. Academic Performance Analysis

* Calculates total marks across Math, Science, and English.
* Calculates each student's average marks.
* Identifies the student with the highest average.
* Calculates the average marks for each subject.

### 3. Attendance Analysis

Groups students according to attendance:

* **Low:** Up to 75%
* **Medium:** Above 75% and up to 90%
* **High:** Above 90% and up to 100%

The program calculates the average marks for each attendance group.

### 4. Data Visualization

The project generates three visualizations:

* **Subject Average Bar Chart:** Compares average marks across subjects.
* **Study Hours vs. Average Marks:** Explores the relationship between daily study hours and academic performance.
* **Correlation Heatmap:** Displays correlations between subject marks, attendance, study hours, and average marks.

## 📋 Dataset Requirements

Place your CSV dataset at:

`data/students.csv`

The dataset should contain these columns:

| Column      | Description           |
| ----------- | --------------------- |
| Name        | Student's name        |
| Math        | Mathematics marks     |
| Science     | Science marks         |
| English     | English marks         |
| Attendance  | Attendance percentage |
| Study_Hours | Daily study hours     |

The code assumes subject marks and attendance are on a 0–100 scale.

## ⚙️ Installation and Setup

### Step 1: Install Python

Install Python 3 if it is not already installed.

### Step 2: Open the project directory

Open PowerShell or a terminal inside the project folder.

### Step 3: Create a virtual environment

```powershell
python -m venv .venv
```

### Step 4: Activate the virtual environment

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 5: Install the required libraries

```powershell
python -m pip install numpy pandas matplotlib seaborn
```

### Step 6: Run the project

```powershell
python main.py
```

## 📂 Output Files

After successful execution, check the `outputs/` directory for:

* `student_analysis.csv` — student records with calculated totals, averages, and attendance groups.
* `
