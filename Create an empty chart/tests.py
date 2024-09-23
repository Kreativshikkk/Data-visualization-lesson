import unittest


class TestChartSettings(unittest.TestCase):

    def __init__(self, methodName='runTest', fig=None, ax=None):
        super().__init__(methodName)
        self.fig = fig
        self.ax = ax

    def setUp(self):
        pass

    def test_figsize(self):
        self.assertEqual(self.fig.get_size_inches().tolist(), [10, 6],
                         f'Expected figsize (10, 6), but got {self.fig.get_size_inches().tolist()}')

    def test_xlabel(self):
        self.assertEqual(self.ax.get_xlabel(), 'Game genre',
                         f'Expected X axis label "Game genre", but got {self.ax.get_xlabel()}')

    def test_ylabel(self):
        self.assertEqual(self.ax.get_ylabel(), 'Amount of games',
                         f'Expected Y axis label "Amount of games", but got {self.ax.get_ylabel()}')

    def test_title(self):
        self.assertEqual(self.ax.get_title(), 'Number of games per genre',
                         f'Expected title "Number of games per genre", but got {self.ax.get_title()}')

    def test_legend_exists(self):
        legend = self.ax.get_legend()
        self.assertIsNotNone(legend, 'Expected a legend, but none was found')

    def test_legend_title(self):
        legend = self.ax.get_legend()
        self.assertEqual(legend.get_title().get_text(), 'Genre',
                         f'Expected legend title "Genre", but got {legend.get_title().get_text()}')

    def test_legend_location(self):
        legend = self.ax.get_legend()
        self.assertEqual((legend.get_bbox_to_anchor()._bbox.x0, legend.get_bbox_to_anchor()._bbox.y0), (1, 0.5),
                         f'Expected legend location (1, 0.5), but got ({legend.get_bbox_to_anchor()._bbox.x0}, {legend.get_bbox_to_anchor()._bbox.y0})')

    def test_legend_loc(self):
        legend = self.ax.get_legend()
        self.assertEqual(legend._loc, 7,
                         f'Expected legend location "center right" (7), but got {legend._loc}')


if __name__ == '__main__':
    unittest.main()
