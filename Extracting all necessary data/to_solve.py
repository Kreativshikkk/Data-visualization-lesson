import matplotlib.pyplot as plt
from matplotlib.colors import to_hex
import pandas as pd
import tests

df = pd.read_csv('dataset.csv')

all_platforms = {'PS4': [],
                 'XOne': [],
                 'PC': [],
                 'WiiU': []}

cmap = plt.get_cmap('tab20c')

colors = {}
"""
Fill the dictionary for the data - all_platforms with some values, 
sorted by indexes and the dictionary for the colors - colors.
"""

tester = tests.Tests(all_platforms, colors)
