import numpy as np
from matplotlib.colors import to_hex
import matplotlib.pyplot as plt
import unittest


class TestChart(unittest.TestCase):

    def __init__(self, runMethod='runTest', fig=None, ax=None):
        super().__init__(runMethod)
        self.fig = fig
        self.ax = ax

    def setUp(self):
        pass

    def test_verify_bars(self):
        self.assertEqual(self.ax.get_title(), 'Number of games per genre for PS4', f'Expected title "Number of games per genre for PS4", but got {self.ax.get_title()}')
        self.assertEqual(self.ax.get_xlabel(), 'Genres', f'Expected X axis label "Genres", but got {self.ax.get_xlabel()}')
        self.assertEqual(self.ax.get_ylabel(), 'Number of games', f'Expected Y axis label "Number of games", but got {self.ax.get_ylabel()}')
        self.assertEqual(len(self.ax.patches), 12, f'Expected 12 bars, but got {len(self.ax.patches)}')

        expected_positions = np.arange(12) * (0.2 + 0.1) - 0.1
        expected_heights = [142, 28, 17, 19, 9, 1, 18, 52, 38, 6, 42, 5]
        for bar, expected_height, expected_position in zip(self.ax.patches, expected_heights, expected_positions):
            self.assertEqual(bar.get_height(), expected_height, f'Expected bar height {expected_height}, but got {bar.get_height()}')
            self.assertAlmostEqual(bar.get_x(), expected_position, places=4, msg=f'Expected bar position {expected_position}, but got {bar.get_x()}')

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
            self.assertEqual(actual_length, expected_length, f'Expected length {expected_length}, but got {actual_length}')


if __name__ == '__main__':
    unittest.main()
