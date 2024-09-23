# Theory
At this step we will do the most of the work we have to. We will extend the previous step for all platforms.

Here we have to pay more attention for `x_positions` argument, because we also have to keep intervals between different platforms. It is: `distance_between_platforms = 1`.
At this step you are supposed to set labels for the platforms along the X-axis. So you have to calculate `x_labels, labels_positions` lists. Positions will be the middle of all positions of the bars which are related to the platform. And at each iteration you have to append the following values:
```python
labels_positions.append(start_x + (bars_amount * (bar_width + spacing) - spacing) / 2)
x_labels.append(platform)
```
Where `platform` is the name of the platform, `start_x` is the `x` position of the first bar related to the particular platform, `bars_amount` is the amount of bars related to the platform, `bar_width` is the width of the bar, `spacing` is the distance between the bars related to the same platform.

In order to set them on the X-axis, you have to use the following code:
```python
ax.set_xticks(labels_positions)
ax.set_xticklabels(x_labels)
```

And, respectively, you have to renew `start_x` as follows:
```python
start_x += (bar_width + spacing) * bars_amount + distance_between_platforms - spacing
```

# Task

Build the bar chart. Do not change arguments that initialize x coordinates of the bars.

- Set X-axis label as `platform`
- Set Y-axis label as `count`
- Left the legend from the last step without changes
- Set platform labels as was discussed in the theory
- Initialize bars for each platform as follows:
```python
ax.bar(x_positions, genre_counts.values, color=genre_colors, width=bar_width, edgecolor='white')
```