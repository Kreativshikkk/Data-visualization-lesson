## Theory

We are gonna learn how to read `.csv` files using `Pandas`. Import can be done as follows:

```python
import pandas as pd

data = pd.read_csv('file_name.csv')
```

And in `data` variable we'll have Dataframe object. We can apply boolean masks for it and:

```python
ps4 = data[data['platform'] == 'PS4']
```

get Dataframe for only `PS4` platform. We can also index it and get all necessary data, for example:

```python
ps4_genres = data[data['platform'] == 'PS4']['genre']
```

gives us Series object with genre data for only `PS4` platform. We can think about Series as a Python dictionary
with `.index` for keys and `.values` for its values. In order to calculate how much each genre appears in the Series we
can use method `.value_counts()`:

```python
genre_counts = ps4_genres.value_counts()
```

And it gives us Series with the amount of appearances of each genre. Finally, we can sort these objects by indices and values. For this
there are methods `sort_index()` and `sort_values()` respectively.

## Task
You have to import dataset into your file, find and calculate the following things:
1. Amount of genres in the whole dataframe
2. Amount of genres in PC platform
3. The list of all genres in sorted order
4. Amount of games of each genre in PS4 platform in sorted order