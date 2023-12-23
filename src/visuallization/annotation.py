import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import seaborn as sns
import random
import numpy as np

# Import dataset 
midwest = pd.read_csv("/Users/nghiempt/Observation/sr-ftq/src/visuallization/data_collected.csv")

# Prepare Data 
# Create as many colors as there are unique midwest['category']
categories = np.unique(midwest['data_type'])
colors = [plt.cm.tab10(i/float(len(categories)-1)) for i in range(len(categories))]

# Draw Plot for Each Category
plt.figure(figsize=(16, 10), dpi= 80, facecolor='w', edgecolor='k')

for i, data_type in enumerate(categories):
    plt.scatter('area', 'poptotal', 
                data=midwest.loc[midwest.data_type==data_type, :], 
                s=20, c=colors[i], label=str(data_type))

# Decorations
plt.gca().set(xlim=(0.0, 0.1), ylim=(0, 90000),
              xlabel='Area', ylabel='Population')

plt.xticks(fontsize=12); plt.yticks(fontsize=12)
plt.title("Number of App Collecting Data", fontsize=22)
plt.legend(fontsize=12)    
plt.show()  