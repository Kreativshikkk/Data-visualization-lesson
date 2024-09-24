import unittest
import matplotlib.pyplot as plt
from matplotlib.colors import to_hex
import pandas as pd
from tests import TestCompareDictionaries

path_to_file = ''
df = pd.read_csv(path_to_file)

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

suite = unittest.TestSuite()
suite.addTest(TestCompareDictionaries('test_compare_dictionaries', data=all_platforms, colors=colors))

runner = unittest.TextTestRunner()
runner.run(suite)
