import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample Dataset
data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Age": [20, 21, 22, 23, 24],
    "Marks": [80, 90, 85, 70, 95]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

# 📈 Line Plot
plt.figure()
plt.plot(df["Name"], df["Marks"])
plt.title("Marks Line Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# 📊 Bar Chart
plt.figure()
plt.bar(df["Name"], df["Marks"])
plt.title("Marks Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# 📉 Histogram
plt.figure()
plt.hist(df["Marks"])
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# 🔥 Seaborn Scatter Plot
plt.figure()
sns.scatterplot(x="Age", y="Marks", data=df)
plt.title("Age vs Marks")
plt.show()