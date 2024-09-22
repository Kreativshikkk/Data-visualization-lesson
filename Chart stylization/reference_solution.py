import unittest
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.colors import to_hex
from tests import StyleTest

bar_width = 0.2
spacing = 0.01
distance_between_platforms = 1
max_count = 0
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
    max_count = max(max_count, all_platforms[platform].max())

fig, ax = plt.subplots(figsize=(10, 6))

"""Make the chart stylization"""

# Span the chart horizontally
for y in range(0, max_count, 20):
    ax.axhspan(y, y + 19, color='#f3e5f5', alpha=0.3)

x_labels = []
labels_positions = []

for platform, genre_counts in all_platforms.items():
    genre_colors = [colors[genre] for genre in genre_counts.index]

    # Calculate the x positions for the bars and the labels
    x_positions = np.arange(start_x, start_x + len(genre_counts) * (bar_width + spacing) - spacing, bar_width + spacing)
    labels_positions.append(start_x + (len(genre_counts) * (bar_width + spacing) - spacing) / 2)
    x_labels.append(platform)

    # Update the start_x for the next platform
    start_x += (bar_width + spacing) * len(genre_counts) + distance_between_platforms - spacing

    # Plot the bars
    ax.bar(x_positions, genre_counts.values, color=genre_colors, width=bar_width, edgecolor='white')

# Labeling
ax.set_xlabel('platform')
ax.set_ylabel('count')

# Create the legend
legend_labels = [plt.Line2D([0, 1], [0, 0], color=colors[genre], lw=5) for genre in
                 df['genre'].value_counts().sort_index().index]
ax.legend(legend_labels, df['genre'].value_counts().sort_index().index, loc='center left', bbox_to_anchor=(1, 0.5), title='genre', frameon=False)

# Remove the chart frame
for spine in ax.spines.values():
    spine.set_visible(False)

# Set the platform names
ax.set_xticks(labels_positions)
ax.set_xticklabels(x_labels)
ax.tick_params(bottom=False, left=False)  # Remove the ticks along the axes

# Move the chart
plt.subplots_adjust(left=0.07, right=0.85, top=1, bottom=0.08)

plt.show()

suite = unittest.TestSuite()
suite.addTest(StyleTest('test_verify_bars', fig=fig, ax=ax))
suite.addTest(StyleTest('test_verify_legend', fig=fig, ax=ax))
suite.addTest(StyleTest('test_features_testing', fig=fig, ax=ax))

runner = unittest.TextTestRunner()
runner.run(suite)
