import unittest
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.colors import to_hex
from tests import TestChart

bar_width = 0.2
spacing = 0.1
distance_between_platforms = 1
start_x = 0  # This variable sets up the x coordinate of the first bar for each platform,
# i.e. should be recalculated for each platform

df = pd.read_csv('../dataset.csv')

all_platforms = {'PS4': [],
                 'XOne': [],
                 'PC': [],
                 'WiiU': []}

cmap = plt.get_cmap('tab20c')

all_genres = sorted(df['genre'].unique())
colors = {genre: to_hex(cmap(i / len(all_genres))) for i, genre in enumerate(all_genres)}


def fill_empty_colors_with_zero_bar(genre_counts):
    for genre in colors.keys():
        if genre not in genre_counts.index:
            genre_counts[genre] = 0
    return genre_counts.sort_index()


for platform in all_platforms:
    all_platforms[platform] = df[df['platform'] == platform]['genre'].value_counts().sort_index()
    if len(all_platforms[platform]) < len(colors):
        all_platforms[platform] = fill_empty_colors_with_zero_bar(all_platforms[platform])

fig, ax = plt.subplots(figsize=(10, 6))

"""You have all_platform dictionary in which data about genres for all platforms is stored,
colors dictionary for colors for each genre. Now, plot the chart for all platforms"""

suite = unittest.TestSuite()
suite.addTest(TestChart('verify_plot', fig=fig, ax=ax))
suite.addTest(TestChart('verify_legend', fig=fig, ax=ax))

runner = unittest.TextTestRunner()
runner.run(suite)
