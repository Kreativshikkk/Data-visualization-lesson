import pandas as pd
import tests
import unittest

path_to_file = ''
df = pd.read_csv(path_to_file)

"""
Write your code here. Solve the task from .md file by changing values of the following variables
1. Int: Amount of genres in the whole dataframe (genres_all_dataframe)
2. Int: Amount of genres in PC platform (genres_pc)
3. List: The list of all genres in sorted order (all_genres)
4. Series: Amount of games of each genre in PS4 platform (genres_ps4) in sorted order
"""

genres_all_dataframe = 0
genres_pc = 0
all_genres = pd.Series([])
genres_ps4 = pd.Series([])

suite = unittest.TestSuite()
suite.addTest(tests.TestGenres('test_genres_all_dataframe', genres_all_dataframe=genres_all_dataframe))
suite.addTest(tests.TestGenres('test_genres_pc', genres_pc=genres_pc))
suite.addTest(tests.TestGenres('test_all_genres', all_genres=all_genres))
suite.addTest(tests.TestGenres('test_genres_ps4', genres_ps4=genres_ps4))

runner = unittest.TextTestRunner()
runner.run(suite)
