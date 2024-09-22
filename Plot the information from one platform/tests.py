import numpy as np


class Test:
    def __init__(self, fig, ax):
        self.fig = fig
        self.ax = ax
        self.verify_bars()

    def verify_bars(self):
        assert self.ax.get_title() == 'Number of games per genre for PS4', f'Expected title "Number of games per genre for PS4", but got {self.ax.get_title()}'
        assert self.ax.get_xlabel() == 'Genres', f'Expected X axis label "Genres", but got {self.ax.get_xlabel()}'
        assert self.ax.get_ylabel() == 'Number of games', f'Expected Y axis label "Number of games", but got {self.ax.get_ylabel()}'
        assert len(self.ax.patches) == 12, f'Expected 12 bars, but got {len(self.ax.patches)}'

        expected_positions = np.arange(12) * (0.2 + 0.1) - 0.1
        expected_heights = [142, 28, 17, 19, 9, 1, 18, 52, 38, 6, 42, 5]
        for bar, expected_height, expected_position in zip(self.ax.patches, expected_heights, expected_positions):
            assert bar.get_height() == expected_height, f'Expected bar height {expected_height}, but got {bar.get_height()}'
            assert np.round(bar.get_x(), 4) == np.round(expected_position, 4), f'Expected bar position {expected_position}, but got {bar.get_x()}'
