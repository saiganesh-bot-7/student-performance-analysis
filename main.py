import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Locate project files
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "students.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

# Load student dataset
df = pd.read_csv(DATA_FILE)

print("\n===== STUDENT DATA =====")
print(df.head())

# Explore dataset
print("\nDataset shape:", df.shape)
print("\nColumn names:", df.columns.tolist())

print("\n===== STATISTICAL SUMMARY =====")
print(df.describe())

# Check missing values
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# Calculate total and average marks
subjects = ["Math", "Science", "English"]

df["Total_Marks"] = df[subjects].sum(axis=1)
df["Average_Marks"] = np.round(
    df[subjects].mean(axis=1), 2
)

print("\n===== STUDENT RESULTS =====")
print(
    df[["Name", "Total_Marks", "Average_Marks"]]
    .to_string(index=False)
)

# Find top-performing student
top_student = df.loc[df["Average_Marks"].idxmax()]

print("\n===== TOP STUDENT =====")
print("Name:", top_student["Name"])
print("Average marks:", top_student["Average_Marks"])

# Calculate subject averages
subject_averages = df[subjects].mean()

print("\n===== SUBJECT AVERAGES =====")
print(subject_averages.round(2))

# Analyze attendance groups
df["Attendance_Group"] = pd.cut(
    df["Attendance"],
    bins=[0, 75, 90, 100],
    labels=["Low", "Medium", "High"],
    include_lowest=True
)

attendance_analysis = df.groupby(
    "Attendance_Group",
    observed=False
)["Average_Marks"].mean()

print("\n===== ATTENDANCE ANALYSIS =====")
print(attendance_analysis.round(2))

# Save analyzed data
df.to_csv(
    OUTPUT_DIR / "student_analysis.csv",
    index=False
)

# Chart 1: Subject averages
plt.figure(figsize=(8, 5))
subject_averages.plot(kind="bar", edgecolor="black")

plt.title("Average Marks by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.ylim(0, 100)
plt.tight_layout()

plt.savefig(OUTPUT_DIR / "subject_averages.png", dpi=150)
plt.show()

# Chart 2: Study hours versus marks
plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="Study_Hours",
    y="Average_Marks",
    s=100
)

plt.title("Study Hours vs Average Marks")
plt.xlabel("Daily Study Hours")
plt.ylabel("Average Marks")
plt.tight_layout()

plt.savefig(OUTPUT_DIR / "study_vs_marks.png", dpi=150)
plt.show()

# Chart 3: Correlation heatmap
correlation = df[
    subjects + ["Attendance", "Study_Hours", "Average_Marks"]
].corr()

plt.figure(figsize=(9, 6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    vmin=-1,
    vmax=1
)

plt.title("Student Performance Correlation")
plt.tight_layout()

plt.savefig(OUTPUT_DIR / "correlation_heatmap.png", dpi=150)
plt.show()

print("\n===== PROJECT COMPLETED SUCCESSFULLY! =====")
print("Output folder:", OUTPUT_DIR)