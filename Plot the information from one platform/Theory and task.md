# Theory
In this step we are gonna build a bar chart only for `PS4` platform. It is guaranteed, that all genres are "non-empty" so you don't have to create zero-height bars at the chart. Let's talk about how to make the legend as in the example chart.

At the second step we considered `matplotlib`'s `Line2D` objects. So we want to initialize them and put as the legend `handles` and put the list of corresponding colors as legend `labels`.
Let's agree that each color will be an object with these parameters:
```python
plt.Line2D([0, 1], [0, 0], color=colors[genre], lw=5)
```
Where `colors` is the dictionary we got at the previous step. 

In order to plot bars you have to call:
```python
ax.bar(x_positions, values, color=genre_colors, width=bar_width, edgecolor='white', label='label')
```
Here:
- `x_positions` - x coordinates of **centers** of bars
- `values` - bars height
- `color` argument sets colors for bars
- `width` sets bars width
- `edgecolor` sets the color of bars edges
- `label` sets the label of bars (so that we can use it for example while creating a legend. At this points we actually don't have to set up `label` for bars)

Let's again agree on the following: the distance between bars is: `spacing = 0.1` and `bar_width = 0.2`. Make your `x_positions` array starting from `0`.
# Task

Build a bar chart for the `PS4` platform. The chart should show the number of games released for each genre. The chart should have the following features:

- Title: `Number of games per genre for PS4`
- X-axis label: `Genres`
- Y-axis label: `Number of games`
- Legend should contain all information about used colors, its `loc` arguement should be `'best'`
