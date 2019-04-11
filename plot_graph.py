import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Bring some raw data.
frequencies = [365, 892, 1112, 954, 705, 463, 283, 135, 68, 35]
# In my original code I create a series and run on that, 
# so for consistency I create a series from the list.
freq_series = pd.Series.from_array(frequencies)

x_labels = ['80-90', '90-100', '100-110', '110-120', '120-130', '130-140',
            '140-150', '150-160', '160-170', '170-180']

# Plot the figure.
#plt.xticks(x_labels,  ha='right', rotation=55, fontsize=20, fontname='monospace')
plt.figure(figsize=(8,12))
ax = freq_series.plot(kind='bar')
#ax.set_title('Amount Frequency')
ax.set_xlabel('SBP Value (mmHg)',fontsize = 20)
ax.set_ylabel('Frequency',fontsize = 20)
ax.set_xticklabels(x_labels,fontsize = 13)

ax.tick_params(axis='both', which='major', labelsize=13)

# Make some labels.
#labels = ["label%d" % i for i in xrange(len(rects))]

# for rect, label in zip(rects, labels):
#     height = rect.get_height()
#     ax.text(rect.get_x() + rect.get_width() / 2, height + 5, label,
#             ha='center', va='bottom')

plt.savefig("image.png")