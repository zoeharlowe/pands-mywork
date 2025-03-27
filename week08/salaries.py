# salaries.py
# This program makes a list of 10 random numbers (between 20000 and 80000) and outputs a list of those salaries and the average of those salaries.
# Author: Zoe McNamara Harlowe

import numpy as np

min_salary = 20000
max_salary = 80000
number_of_salaries = 10

np.random.seed(1)
salaries = np.random.randint(min_salary, max_salary, number_of_salaries)

salaries_plus = salaries + 5000

salaries_increase = salaries * 1.05
salaries_increase = salaries_increase.astype(int)

print(salaries_increase)