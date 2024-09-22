import matplotlib.pyplot as plt
from matplotlib.colors import to_hex
import pandas as pd

class Tests:
    def __init__(self, data, colors):
        self.data = data
        self.colors = colors
        self.compare_dictionaries()

    def compare_dictionaries(self):
        df = pd.read_csv('../dataset.csv')

        cmap = plt.get_cmap('tab20c')

        all_genres = sorted(df['genre'].unique())
        colors = {genre: to_hex(cmap(i / len(all_genres))) for i, genre in enumerate(all_genres)}
        data_correct = {'PS4': [],
                 'XOne': [],
                 'PC': [],
                 'WiiU': []}

        all_platforms = {'PS4': [],
                         'XOne': [],
                         'PC': [],
                         'WiiU': []}

        def fill_empty_colors_with_zero_bar(genre_counts):
            for genre in colors.keys():
                if genre not in genre_counts.index:
                    genre_counts[genre] = 0
            return genre_counts.sort_index()

        for platform in all_platforms:
            all_platforms[platform] = df[df['platform'] == platform]['genre'].value_counts().sort_index()
            if len(all_platforms[platform]) < len(colors):
                all_platforms[platform] = fill_empty_colors_with_zero_bar(all_platforms[platform])

        def compare_dicts_of_series(dict1, dict2):
            if dict1.keys() != dict2.keys():
                return False
            for key in dict1:
                if not dict1[key].equals(dict2[key]):
                    return False
            return True

        assert compare_dicts_of_series(self.data, all_platforms) == True
        assert self.colors == colors
