import pandas as pd


class Tests:
    def __init__(self, genres_all_dataframe, genres_pc, all_genres, genres_ps4):
        self.df = pd.read_csv('../dataset.csv')
        self.genres_all_dataframe = len(self.df['genre'].unique())
        self.genres_pc = len(self.df[self.df['platform'] == 'PC']['genre'].unique())
        self.all_genres = sorted(self.df['genre'].unique())
        self.genres_ps4 = self.df[self.df['platform'] == 'PS4']['genre'].value_counts().sort_index()
        self.test_genres_all_dataframe(genres_all_dataframe)
        self.test_genres_pc(genres_pc)
        self.test_all_genres(all_genres)
        self.test_genres_ps4(genres_ps4)

    def test_genres_all_dataframe(self, genres_all_dataframe):
        assert genres_all_dataframe == self.genres_all_dataframe, f'Expected {self.genres_all_dataframe}, but got {genres_all_dataframe}'

    def test_genres_pc(self, genres_pc):
        assert genres_pc == self.genres_pc, f'Expected {self.genres_pc}, but got {genres_pc}'

    def test_all_genres(self, all_genres):
        assert all_genres == self.all_genres, f'Expected {self.all_genres}, but got {all_genres}'

    def test_genres_ps4(self, genres_ps4):
        assert genres_ps4.equals(self.genres_ps4), f'Expected {self.genres_ps4}, but got {genres_ps4}'
