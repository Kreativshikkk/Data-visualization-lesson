# Theory
This step is not that general as previous ones. This one is more specific for our task. We will try to extract the data we need for building the chart from the dataset and then associate some colors for the bars in the chart.

The supposed format for storing data is as follows: since we have `4` different platforms with the same characteristics, let's put them all in `Python` dictionary, where keys are platform names and values are the data corresponding to the platform.

For values in this dictionary we can use `.value_counts()`, because those are literally `Series` objects with "keys" equal to genres and "values" equal to the amount of each genre.

So for values in the dictionary we have something like this:
```python
all_platforms[platform] = df[df['Platform'] == platform]['Genre'].value_counts()
```
Where `all_platforms` is the dictionary, `df` is the imported dataset, `platform` is the name of the platform.

Now let's talk about colors. Let's now just keep them in dictionary as well (the usage will be in further steps). We have genres as keys and colors as values. There are multiple ways to initialize values objects. We'll use:
```python
import matplotlib.pyplot as plt
cmap = plt.get_cmap('')
```
It gives us `colormap`. It maps the fraction to the color:
```python
import matplotlib.pyplot as plt
from matplotlib.colors import to_hex 
cmap = plt.get_cmap('tab20c')
# Assume we have the list of all genres in sorted order: all_genres
# Then we have such pairs in our dictionary: {genre: to_hex(cmap(i / len(all_genres))) for i, genre in enumerate(all_genres)}
```

It is important for us to notice, that if the platform has `0` games in some genre, then it has to have an empty bar in the chart. So that the particular genre is not skipped. For this let's use such a function:
```python
def fill_empty_colors_with_zero_bar(genre_counts):
    for genre in colors.keys():
        if genre not in genre_counts.index:
            genre_counts[genre] = 0
    return genre_counts.sort_index()
```
where `genre_counts` is the Series object, `colors` is the dictionary with colors.

# Task
Create the dictionary for the data (so that its values - Series objects are sorted by indexes) and the dictionary for the colors (use `tab20c` colormap).