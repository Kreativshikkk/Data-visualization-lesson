import matplotlib.pyplot as plt
import tests

"""
Write your code here. Solve the task from .md file by setting figure and axes up
"""

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 2, 3], label='test')

tester = tests.Tests(fig, ax)