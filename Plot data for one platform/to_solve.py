import unittest
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.colors import to_hex
from tests import TestChart

bar_width = 0.2
spacing = 0.1
df = pd.read_csv('../dataset.csv')
ps4_genre_counts = []
cmap = plt.get_cmap('tab20c')

all_genres = sorted(df['genre'].unique())
colors = {genre: to_hex(cmap(i / len(all_genres))) for i, genre in enumerate(all_genres)}
fig, ax = plt.subplots(figsize=(10, 6))

"""You have colors dictionary from the previous step.
Write your bars plotting, axes labeling and titling, legend initialization for PS4 platform here"""

suite = unittest.TestSuite()
suite.addTest(TestChart('test_verify_bars', fig=fig, ax=ax))
suite.addTest(TestChart('test_verify_legend', fig=fig, ax=ax))

runner = unittest.TextTestRunner()
runner.run(suite)
