import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.colors import to_hex
import tests

bar_width = 0.2
spacing = 0.1
df = pd.read_csv('../dataset.csv')
ps4_genre_counts = []
cmap = plt.get_cmap('tab20c')

all_genres = sorted(df['genre'].unique())
colors = {genre: to_hex(cmap(i / len(all_genres))) for i, genre in enumerate(all_genres)}
fig, ax = plt.subplots(figsize=(10, 6))

"""You have colors dictionary from the previous step.
Write your bars plotting, axes labeling and titling, legend initialization here"""

# Get the amount of games of each genre for PS4 platform
ps4_genre_counts = df[df['platform'] == 'PS4']['genre'].value_counts().sort_index()

# Plot the bars
genre_colors = [colors[genre] for genre in ps4_genre_counts.index]
x_positions = np.arange(len(ps4_genre_counts)) * (bar_width + spacing)
ax.bar(x_positions, ps4_genre_counts.values, color=genre_colors, width=bar_width, edgecolor='white')

# Labeling
ax.set_title('Number of games per genre for PS4')
ax.set_xlabel('Genres')
ax.set_ylabel('Number of games')

# Create the legend
legend_labels = [plt.Line2D([0, 1], [0, 0], color=colors[genre], lw=5) for genre in
                 df['genre'].value_counts().sort_index().index]
ax.legend(legend_labels, df['genre'].value_counts().sort_index().index, loc='best')

plt.show()

tests.Test(fig, ax)
