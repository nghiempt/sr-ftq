import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import seaborn as sns
import random
import numpy as np

# Import Data
df_raw = pd.read_csv("/Users/nghiempt/Observation/sr-ftq/src/visuallization/data_collected.csv")

# Prepare Data
df = df_raw.groupby('data_type').size().reset_index(name='counts')
n = df['data_type'].unique().__len__() + 1
all_colors = list(plt.cm.colors.cnames.keys())
random.seed(100)
c = random.choices(all_colors, k=n)

# Create a color dictionary for the legend
color_dict = dict(zip(df['data_type'], c))

# Plot Bars
plt.figure(figsize=(10, 10), dpi=100)
bar_container = plt.bar(df['data_type'], df['counts'], color=[color_dict[val] for val in df['data_type']], width=.5)

# Create a legend
plt.legend([plt.Rectangle((0,0),1,1, color=color_dict[label]) for label in df['data_type']], df['data_type'].tolist())

# Add Scatter Plot (optional)
# plt.scatter(df['data_type'], df['counts'], color='red')

# Add Annotations (optional)
# for i, (x, y) in enumerate(zip(df['data_type'], df['counts'])):
#     plt.annotate(f'({x}, {y})', (i, y), textcoords="offset points", xytext=(0,10), ha='center')

# Decoration
plt.gca().set_xticklabels(df['data_type'], rotation=60, horizontalalignment='right')
plt.title("Number of Apps Collecting Data", fontsize=20)
plt.ylabel('Number of Apps Collecting Data', fontsize=14)
plt.ylim(0, max(df['counts']) * 1.1)  # Adjust the y limit to make room for annotations
plt.show()
