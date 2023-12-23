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
n = df['data_type'].unique().__len__()+1
all_colors = list(plt.cm.colors.cnames.keys())
random.seed(100)
c = random.choices(all_colors, k=n)

# Plot Bars
plt.figure(figsize=(10,10), dpi= 80)
plt.bar(df['data_type'], df['counts'], color=c, width=.5)
for i, data_type in enumerate(df['counts'].values):
    plt.text(i, data_type, float(data_type), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':12})
    
# Decoration
plt.gca().set_xticklabels(df['data_type'], rotation=60, horizontalalignment= 'right')
plt.title("Number of App Collecting Data", fontsize=18)
plt.ylabel('Number of App Collecting Data', fontsize=12)
plt.ylim(0, 500)
plt.show()
