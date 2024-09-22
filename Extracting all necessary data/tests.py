import matplotlib.pyplot as plt
from matplotlib.colors import to_hex
import pandas as pd
import unittest


class TestCompareDictionaries(unittest.TestCase):
    def __init__(self, methodName='runTest', data=None, colors=None):
        super().__init__(methodName)
        self.to_test_data = data
        self.to_test_colors = colors

    def setUp(self):
        df = pd.read_csv('../dataset.csv')

        cmap = plt.get_cmap('tab20c')

        all_genres = sorted(df['genre'].unique())
        self.expected_colors = {genre: to_hex(cmap(i / len(all_genres))) for i, genre in enumerate(all_genres)}

        self.expected_data = {'PS4': [],
                              'XOne': [],
                              'PC': [],
                              'WiiU': []}

        def fill_empty_colors_with_zero_bar(genre_counts):
            for genre in self.expected_colors.keys():
                if genre not in genre_counts.index:
                    genre_counts[genre] = 0
            return genre_counts.sort_index()

        for platform in self.expected_data:
            self.expected_data[platform] = df[df['platform'] == platform]['genre'].value_counts().sort_index()
            if len(self.expected_data[platform]) < len(self.expected_colors):
                self.expected_data[platform] = fill_empty_colors_with_zero_bar(self.expected_data[platform])

    def test_compare_dictionaries(self):

        def compare_dicts_of_series(dict1, dict2):
            if dict1.keys() != dict2.keys():
                return False
            for key in dict1:
                if not dict1[key].equals(dict2[key]):
                    return False
            return True

        self.assertTrue(compare_dicts_of_series(self.expected_data, self.to_test_data))
        self.assertEqual(self.to_test_colors, self.expected_colors)


if __name__ == '__main__':
    unittest.main()
