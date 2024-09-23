# Theory
After this step you will learn how to build an empty chart using `matplotlib` and set it up. Namely, we'll consider legends, X and Y titles, chart label.

You have several options to create a chart. Further we will consider this one:
```python
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
```
This method of initialization returns Figure and Axes object, so that it is easier to edit the plot parameters.
Figure is the top-level container of all the axes and properties of a plot, Axes is the encapsulation of all elements of an individual plot of a figure.
When initializing new plot, we can set its size:
```python
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(10, 6))
```
Now let's talk about Axes settings. In order to create X or Y label you have to call these methods:
```python
ax.set_xlabel('x_label')
ax.set_ylabel('y_label')
```

In order to create a legend for the plot you have to call `ax.legend`:
```python
ax.legend(handles, labels, loc='center left', bbox_to_anchor=(1, 0.5), title='genre', frameon=False)
```
This line creates a new legend using handles for the corresponding plot elements and labels for their descriptions. The legend is positioned such that its center-left point is anchored to the middle of the right side of the chart.
The title of the legend is `genre` and its frame is not visible.

You can create a legend without using `handles` and `labels`. In this case `matplotlib` will automatically associate all elements with their labels.

`handles` is usually a list of `Line2D` objects, and `labels` is usually a list of corresponding strings.

# Task
You have to create an empty chart with `figsize=(10,6)`, label X axis as `'Game genre'`, Y axis as `'Amount of games'`, set the title of the chart as `'Number of games per genre'` and create a legend with title `'Genre'` located such that its center-right point is anchored to the middle of the right side of the chart.