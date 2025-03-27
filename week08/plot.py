# plot.py
# This program will write a function to plot y=x^2 
# Author: Zoe McNamara Harlowe

def plot():
    import matplotlib.pyplot as plt
    import numpy as np

    xpoints = np.array(range(1,101))
    ypoints = xpoints * xpoints

    plt.plot(xpoints, ypoints)
    plt.show()

plot()