import unittest
import matplotlib.pyplot as plt
from matplotlib.colors import to_hex
import pandas as pd
from tests import TestCompareDictionaries

df = pd.read_csv('../dataset.csv')

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

# Initialize the dictionary for colors using colormap
all_genres = sorted(df['genre'].unique())
colors = {genre: to_hex(cmap(i / len(all_genres))) for i, genre in enumerate(all_genres)}


def fill_empty_colors_with_zero_bar(genre_counts):
    for genre in colors.keys():
        if genre not in genre_counts.index:
            genre_counts[genre] = 0
    return genre_counts.sort_index()


# Fulfill the dictionary for all platforms, setting empty bars if necessary
for platform in all_platforms:
    all_platforms[platform] = df[df['platform'] == platform]['genre'].value_counts().sort_index()
    if len(all_platforms[platform]) < len(colors):
        all_platforms[platform] = fill_empty_colors_with_zero_bar(all_platforms[platform])

suite = unittest.TestSuite()
suite.addTest(TestCompareDictionaries('test_compare_dictionaries', data=all_platforms, colors=colors))

runner = unittest.TextTestRunner()
runner.run(suite)
