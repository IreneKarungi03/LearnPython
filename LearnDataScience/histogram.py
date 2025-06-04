import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data - replace this with your actual dataset
data = {
    'Duration': [45, 45, 60, 30, 45, 120, 60, 60, 30, 45, 30, 45, 60, 45, 60, 30, 180, 210, 60, 45],
    'Pulse': [110, 117, 103, 109, 117, 102, 110, 109, 98, 100, 99, 95, 100, 113, 120, 105, 125, 130, 135, 145]
}

df = pd.DataFrame(data)

# Plotting
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Duration histogram
sns.histplot(df['Duration'], kde=True, bins=15, ax=axes[0], color='skyblue')
axes[0].set_title("Duration Distribution")
axes[0].set_xlabel("Duration")
axes[0].set_ylabel("Count")

# Pulse histogram
sns.histplot(df['Pulse'], kde=True, bins=15, ax=axes[1], color='steelblue')
axes[1].set_title("Pulse Distribution")
axes[1].set_xlabel("Pulse")
axes[1].set_ylabel("Count")

plt.tight_layout()
plt.show()
