# Theory

Here we want to sugarcoat the chart. We are gonna span the chart horizontally, remove the chart frame, X-axis and Y-axis ticks, move the chart and legend a little bit

### Chart spanning
Let's span it as follows: we draw rectangles with a step `20` (actually, `19` in order to make edges less contrast) along the Y-axis. Its transparency is `alpha=0.3` and this <span style="color: #F3E5F5;">color</span>. Spanning can be done as follows:
```python
for y in range(0, max_count, 20):
    ax.axhspan(y, y + 19, color='#f3e5f5', alpha=0.3)
```
Here, `max_count` is the height of the highest bar.

### Removing the chart frame
You can do it with these lines:
```python
for spine in ax.spines.values():
    spine.set_visible(False)
```

### Removing ticks along the X-axis and Y-axis
You can do it with this line:
```python
ax.tick_params(bottom=False, left=False)
```

### Legend improving
In order to remove its frame you have to set argument `frameon=False` while creating the legend. Let's also set its position with following arguments: `loc='center left', bbox_to_anchor=(1, 0.5)`, and, finally, label it as `genre`.
Initialize it with the following line:
```python
ax.legend(handles, labels, loc='center left', bbox_to_anchor=(1, 0.5), title='genre', frameon=False)
```

### Moving and changing the chart
Finally, let's move the chart a little bit, so that the legend is readable and the space is used more rationally. You can do it with this line with these parameters:
```python
plt.subplots_adjust(left=0.07, right=0.85, top=1, bottom=0.08)
```
Change the `spacing` argument's value to `0.01`
# Task
Apply all these changes to your implementation from the previous step.