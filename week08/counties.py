# counties.py
# This program will output a piechart of counties in Ireland
# Author: Zoe McNamara Harlowe

import matplotlib.pyplot as plt
import numpy as np

# Create a list of counties
possible_counties = ['Cork', 'Dublin', 'Kerry', 'Galway', 'Mayo', 'Limerick', 'Clare', 'Wicklow', 'Waterford', 'Kilkenny']

np.random.seed(1)
counties = np.random.choice(possible_counties, 100, p=[0.1, 0.3, 0.2, 0.05, 0.1, 0.1, 0.05, 0.05, 0.025, 0.025])
print(counties)

# Get the unique items and the counts of each
unique, counts = np.unique(counties, return_counts=True)

# Make pie chart
# plt.pie(counts, labels=unique)

# Make bar chart
plt.bar(possible_counties, counts)
plt.show()