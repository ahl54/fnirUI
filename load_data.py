
# coding: utf-8

# In[43]:

import csv

raw_data_path = """raw_data_3000/E1/"""

data = []
with open(raw_data_path + '04031.csv') as f:
    cf = csv.reader(f)
    for row in cf:
        data.append((float(row[3].strip(' "')), float(row[4].strip(' "'))))


# In[65]:

import matplotlib.pyplot as plt
from math import log
data = data[:1544] # manual data cutoff before signal drops
plt.plot(*zip(*data))
plt.show()


# In[ ]:



