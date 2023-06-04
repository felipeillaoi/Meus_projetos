import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

x = [14,15,16,17,18]
y = [1,2,4,4,5]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
    return slope * x + intercept

print()