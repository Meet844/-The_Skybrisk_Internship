import pandas as pd
import numpy as np

# NumPy Array
arr = np.array([10, 20, 30, 40])
print("NumPy Array:", arr)

# Basic operations
print("Mean:", np.mean(arr))
print("Sum:", np.sum(arr))

# Pandas DataFrame
data = {
    "Name": ["A", "B", "C", "D"],
    "Age": [20, 21, None, 23],
    "Marks": [80, 90, 85, None]
}

df = pd.DataFrame(data)
print("\nOriginal Data:")
print(df)

# Data Cleaning (remove missing values)
df_clean = df.dropna()
print("\nCleaned Data:")
print(df_clean)

# Fill missing values
df_filled = df.fillna(df.mean(numeric_only=True))
print("\nFilled Data:")
print(df_filled)

# Average Marks
average_marks = df["Marks"].mean()
print("\nAverage Marks:", average_marks)