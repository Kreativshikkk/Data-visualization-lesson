import unittest
import pandas as pd


class TestGenres(unittest.TestCase):

    def __init__(self, methodName='runTest', genres_all_dataframe=None, genres_pc=None, all_genres=None,
                 genres_ps4=None):
        super().__init__(methodName)
        self.to_test_genres_all_dataframe = genres_all_dataframe
        self.to_test_genres_pc = genres_pc
        self.to_test_all_genres = all_genres
        self.to_test_genres_ps4 = genres_ps4

    def setUp(self):
        self.df = pd.read_csv('../dataset.csv')
        self.expected_genres_all_dataframe = len(self.df['genre'].unique())
        self.expected_genres_pc = len(self.df[self.df['platform'] == 'PC']['genre'].unique())
        self.expected_all_genres = sorted(self.df['genre'].unique())
        self.expected_genres_ps4 = self.df[self.df['platform'] == 'PS4']['genre'].value_counts().sort_index()

    def test_genres_all_dataframe(self):
        self.assertEqual(self.expected_genres_all_dataframe, self.to_test_genres_all_dataframe,
                         f'Expected {self.expected_genres_all_dataframe}, but got {self.to_test_genres_all_dataframe}')

    def test_genres_pc(self):
        self.assertEqual(self.expected_genres_pc, self.to_test_genres_pc,
                         f'Expected {self.expected_genres_pc}, but got {self.to_test_genres_pc}')

    def test_all_genres(self):
        self.assertEqual(self.expected_all_genres, self.to_test_all_genres,
                         f'Expected {self.expected_all_genres}, but got {self.to_test_all_genres}')

    def test_genres_ps4(self):
        pd.testing.assert_series_equal(self.expected_genres_ps4, self.to_test_genres_ps4,
                                       obj=f'Expected {self.expected_genres_ps4}, but got {self.to_test_genres_ps4}')


if __name__ == '__main__':
    unittest.main()
