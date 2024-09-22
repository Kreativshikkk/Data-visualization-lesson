import numpy as np


class Test:
    def __init__(self, fig, ax):
        self.fig = fig
        self.ax = ax
        self.verify_plot()

    def verify_plot(self):
        assert self.ax.get_xlabel() == 'platform', f'Expected X axis label "platform", but got {self.ax.get_xlabel()}'
        assert self.ax.get_ylabel() == 'count', f'Expected Y axis label "count", but got {self.ax.get_ylabel()}'
        assert len(self.ax.patches) == 48, f'Expected 48 bars, but got {len(self.ax.patches)}'

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
        for bar, expected_height, expected_position in zip(self.ax.patches, expected_heights, expected_positions):
            assert bar.get_height() == expected_height, f'Expected bar height {expected_height}, but got {bar.get_height()}'
            assert np.round(bar.get_x(), 4) == np.round(expected_position,
                                                        4), f'Expected bar position {expected_position}, but got {bar.get_x()}'

        for i, x_tick in enumerate(self.ax.get_xticklabels()):
            assert round(x_tick.get_position()[0], 4) == round(expected_labels_positions[i],
                                                4), f'Expected {expected_labels_positions[i]}, but got {x_tick.get_position()[0]}'
            assert x_tick.get_text() == expected_x_labels[
                i], f'Expected {expected_x_labels[i]}, but got {x_tick.get_text()}'
