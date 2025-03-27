# ages.py
# This program will output 10 random ages between 21 and 65 and scatter plot them against the salaries from salaries.py.
# Author: Zoe McNamara Harlowe

import numpy as np  
import matplotlib.pyplot as plt

min_salary = 20000
max_salary = 80000
number_of_salaries = 10

np.random.seed(1)
salaries = np.random.randint(min_salary, max_salary, number_of_salaries)

min_age = 21
max_age = 66
number_of_ages = 10
np.random.seed(1)
ages = np.random.randint(min_age, max_age, number_of_ages)

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

plt.scatter(salaries, ages)
plt.plot(xpoints, ypoints)

plt.xlabel("Salaries")
plt.ylabel("Ages")
plt.legend(["Salaries", "y = x^2"])
plt.title("Random Salaries vs Ages")

plt.savefig("prettier-plot.png")