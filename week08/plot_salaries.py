# plot_salaries.py
# This program will plot a histogram of the salaries from salaries.py
# Author: Zoe McNamara Harlowe

import matplotlib.pyplot as plt
import numpy as np

min_salary = 20000
max_salary = 80000
number_of_salaries = 10

np.random.seed(1)
salaries = np.random.randint(min_salary, max_salary, number_of_salaries)

plt.hist(salaries)
plt.show()


