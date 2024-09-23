import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_hex
import unittest


class TestChart(unittest.TestCase):
    def __init__(self, runMethod='runTest', fig=None, ax=None):
        super().__init__(runMethod)
        self.fig = fig
        self.ax = ax

    def verify_plot(self):
        self.assertEqual(self.ax.get_xlabel(), 'platform',
                         f'Expected X axis label "platform", but got {self.ax.get_xlabel()}')
        self.assertEqual(self.ax.get_ylabel(), 'count',
                         f'Expected Y axis label "count", but got {self.ax.get_ylabel()}')
        self.assertEqual(len(self.ax.patches), 48, f'Expected 48 bars, but got {len(self.ax.patches)}')

        start_x = 0
        expected_positions = np.array([])
        expected_x_labels = ['PS4', 'XOne', 'PC', 'WiiU']
        expected_labels_positions = []
        for i in range(4):
            expected_labels_positions.append(round(start_x + ((0.2 + 0.1) * 12 - 0.1) / 2, 4))
            platform_positions = np.arange(12) * (0.2 + 0.1) - 0.1 + start_x
            expected_positions = np.append(expected_positions, platform_positions)
            start_x += 0.3 * 12 + 1 - 0.1

        expected_heights = [142, 28, 17, 19, 9, 1, 18, 52, 38, 6, 42, 5, 81, 14, 5, 17, 4, 0, 18, 14, 36, 3, 34, 2, 39,
                            8, 2, 3, 1, 0, 13, 18, 21, 18, 11, 17, 35, 3, 2, 13, 7, 3, 1, 4, 3, 0, 2, 0]

        colors = ['#3182bd', '#6baed6', '#c6dbef', '#fd8d3c', '#fdae6b', '#31a354', '#a1d99b', '#c7e9c0', '#9e9ac8', '#dadaeb', '#636363', '#bdbdbd'] * 4

        for bar, expected_height, expected_position, expected_facecolor in zip(self.ax.patches, expected_heights, expected_positions, colors):
            self.assertAlmostEqual(bar.get_width(), 0.2, places=4, msg=f'Expected bar width 0.2, but got {bar.get_width()}')
            self.assertEqual(bar.get_edgecolor(), matplotlib.colors.to_rgba('white'),
                             f'Expected white edge color, but got {bar.get_edgecolor()}')
            self.assertEqual(bar.get_height(), expected_height,
                             f'Expected bar height {expected_height}, but got {bar.get_height()}')
            self.assertAlmostEqual(bar.get_x(), expected_position, places=4,
                                   msg=f'Expected bar position {expected_position}, but got {bar.get_x()}')
            self.assertEqual(to_hex(bar.get_facecolor()), expected_facecolor,
                             f'Expected facecolor {expected_facecolor}, but got {to_hex(bar.get_facecolor())}')

        for i, x_tick in enumerate(self.ax.get_xticklabels()):
            self.assertAlmostEqual(x_tick.get_position()[0], expected_labels_positions[i], places=4,
                                   msg=f'Expected {expected_labels_positions[i]}, but got {x_tick.get_position()[0]}')
            self.assertEqual(x_tick.get_text(), expected_x_labels[
                i], f'Expected {expected_x_labels[i]}, but got {x_tick.get_text()}')

    def verify_legend(self):
        legend = self.ax.get_legend()
        self.assertIsNotNone(legend, 'Expected legend, but none found')

        handles = legend.legend_handles
        labels = [text.get_text() for text in legend.get_texts()]

        expected_labels = ['Action', 'Adventure', 'Fighting', 'Misc', 'Platform', 'Puzzle', 'Racing', 'Role-Playing',
                           'Shooter', 'Simulation', 'Sports', 'Strategy']

        cmap = plt.get_cmap('tab20c')
        colors = {genre: to_hex(cmap(i / 12)) for i, genre in enumerate(expected_labels)}

        self.assertEqual(labels, expected_labels, f'Expected labels {expected_labels}, but got {labels}')

        for handle, label in zip(handles, labels):
            expected_color = colors[label]
            actual_color = to_hex(handle.get_color())
            self.assertEqual(actual_color, expected_color, f'Expected color {expected_color}, but got {actual_color}')
            self.assertEqual(handle.get_linewidth(), 5, f'Expected linewidth 5, but got {handle.get_linewidth()}')

            x_data = handle.get_xdata()
            expected_length = 20
            actual_length = x_data[-1] - x_data[0]
            self.assertEqual(actual_length, expected_length,
                             f'Expected length {expected_length}, but got {actual_length}')
