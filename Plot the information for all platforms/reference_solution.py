import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.colors import to_hex
import tests

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

x_labels = []
labels_positions = []

for platform, genre_counts in all_platforms.items():
    genre_colors = [colors[genre] for genre in genre_counts.index]

    x_positions = np.arange(start_x, start_x + len(genre_counts) * (bar_width + spacing) - spacing, bar_width + spacing)
    labels_positions.append(start_x + (len(genre_counts) * (bar_width + spacing) - spacing) / 2)
    x_labels.append(platform)

    start_x = start_x + (bar_width + spacing) * len(genre_counts) + distance_between_platforms - spacing

    ax.bar(x_positions, genre_counts.values, color=genre_colors, width=bar_width, edgecolor='white')

ax.set_xlabel('platform')
ax.set_ylabel('count')

legend_labels = [plt.Line2D([0, 1], [0, 0], color=colors[genre], lw=5) for genre in
                 df['genre'].value_counts().sort_index().index]
ax.legend(legend_labels, df['genre'].value_counts().sort_index().index, loc='best')

ax.set_xticks(labels_positions)
ax.set_xticklabels(x_labels)

plt.show()

tests.Test(fig, ax)
