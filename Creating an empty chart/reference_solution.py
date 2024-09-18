import matplotlib.pyplot as plt
import tests

"""
Write your code here. Solve the task from .md file by setting figure and axes up
"""

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot([1, 2, 3], [1, 2, 3], label='test')
ax.set_xlabel('Game genre')
ax.set_ylabel('Amount of games')
ax.set_title('Number of games per genre')
ax.legend(title='Genre', loc='center right', bbox_to_anchor=(1, 0.5))

tester = tests.Tests(fig, ax)
