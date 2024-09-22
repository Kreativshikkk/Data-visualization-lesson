import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_hex
import unittest


class StyleTest(unittest.TestCase):
    def __init__(self, runMethod='runTest', fig=None, ax=None):
        super().__init__(runMethod)
        self.fig = fig
        self.ax = ax
        self.spanning_rectangles = []

    def test_verify_bars(self):
        self.assertEqual(self.ax.get_xlabel(), 'platform',
                         f'Expected X axis label "platform", but got {self.ax.get_xlabel()}')
        self.assertEqual(self.ax.get_ylabel(), 'count',
                         f'Expected Y axis label "count", but got {self.ax.get_ylabel()}')

        chart_bars = []
        for rectangle in self.ax.patches:
            if round(rectangle.get_width(), 1) == 0.2:
                chart_bars.append(rectangle)
            else:
                self.spanning_rectangles.append(rectangle)

        self.assertEqual(len(chart_bars), 48, f'Expected 48 bars, but got {len(chart_bars)}')
        self.assertEqual(len(self.spanning_rectangles), 8,
                         f'Expected 8 spanning rectangles, but got {len(self.spanning_rectangles)}')

        start_x = 0
        expected_positions = np.array([])
        expected_x_labels = ['PS4', 'XOne', 'PC', 'WiiU']
        expected_labels_positions = []
        for i in range(4):
            expected_labels_positions.append(round(start_x + ((0.2 + 0.01) * 12 - 0.01) / 2, 4))
            platform_positions = np.arange(12) * (0.2 + 0.01) - 0.1 + start_x
            expected_positions = np.append(expected_positions, platform_positions)
            start_x += 0.21 * 12 + 1 - 0.01

        expected_heights = [142, 28, 17, 19, 9, 1, 18, 52, 38, 6, 42, 5, 81, 14, 5, 17, 4, 0, 18, 14, 36, 3, 34, 2, 39,
                            8, 2, 3, 1, 0, 13, 18, 21, 18, 11, 17, 35, 3, 2, 13, 7, 3, 1, 4, 3, 0, 2, 0]
        for bar, expected_height, expected_position in zip(chart_bars, expected_heights, expected_positions):
            self.assertEqual(bar.get_height(), expected_height,
                             f'Expected bar height {expected_height}, but got {bar.get_height()}')
            self.assertAlmostEqual(bar.get_x(), expected_position, places=4,
                                   msg=f'Expected bar position {expected_position}, but got {bar.get_x()}')

        for i, x_tick in enumerate(self.ax.get_xticklabels()):
            self.assertAlmostEqual(x_tick.get_position()[0], expected_labels_positions[i], places=4,
                                   msg=f'Expected {expected_labels_positions[i]}, but got {x_tick.get_position()[0]}')
            self.assertEqual(x_tick.get_text(), expected_x_labels[i],
                             f'Expected {expected_x_labels[i]}, but got {x_tick.get_text()}')

    def test_verify_legend(self):
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

        self.assertFalse(legend.get_frame_on(), "Expected frameon to be False, but got True")
        self.assertEqual(legend._loc, 6, f"Expected loc to be 'center left' (6), but got {legend._loc}")

        bbox = legend.get_bbox_to_anchor()._bbox
        self.assertEqual(bbox.x0, 1, f"Expected bbox_to_anchor x0 to be 1, but got {bbox.x0}")
        self.assertEqual(bbox.y0, 0.5, f"Expected bbox_to_anchor y0 to be 0.5, but got {bbox.y0}")

    def test_features_testing(self):
        for rect in self.spanning_rectangles:
            self.assertEqual(rect.get_alpha(), 0.3, f'Expected alpha 0.3, but got {rect.get_alpha()}')
            self.assertEqual(to_hex(rect.get_facecolor()), '#f3e5f5',
                             f'Expected facecolor "#f3e5f5", but got {to_hex(rect.get_facecolor())}')

        for spine in self.ax.spines.values():
            self.assertFalse(spine.get_visible(), f'Expected spine to be invisible, but got visible')

        x_ticks_off = all(not tick.tick1line.get_visible() for tick in self.ax.xaxis.get_major_ticks())
        y_ticks_off = all(not tick.tick1line.get_visible() for tick in self.ax.yaxis.get_major_ticks())

        self.assertTrue(x_ticks_off, "X-axis ticks are still visible")
        self.assertTrue(y_ticks_off, "Y-axis ticks are still visible")

        subplot_params = self.ax.figure.subplotpars
        self.assertEqual(subplot_params.left, 0.07,
                         f'Expected left subplot parameter 0.07, but got {subplot_params.left}')
        self.assertEqual(subplot_params.right, 0.85,
                         f'Expected right subplot parameter 0.85, but got {subplot_params.right}')
        self.assertEqual(subplot_params.top, 1, f'Expected top subplot parameter 1, but got {subplot_params.top}')
        self.assertEqual(subplot_params.bottom, 0.08,
                         f'Expected bottom subplot parameter 0.08, but got {subplot_params.bottom}')
