class Tests:
    def __init__(self, fig, ax):
        self.fig = fig
        self.ax = ax
        self.verify_settings()

    def verify_settings(self):
        assert self.fig.get_size_inches().tolist() == [10,
                                                       6], f'Expected figsize (10, 6), but got {self.fig.get_size_inches().tolist()}'

        assert self.ax.get_xlabel() == 'Game genre', f'Expected X axis label "Game genre", but got {self.ax.get_xlabel()}'

        assert self.ax.get_ylabel() == 'Amount of games', f'Expected Y axis label "Amount of games", but got {self.ax.get_ylabel()}'

        assert self.ax.get_title() == 'Number of games per genre', f'Expected title "Number of games per genre", but got {self.ax.get_title()}'

        legend = self.ax.get_legend()
        assert legend is not None, 'Expected a legend, but none was found'
        assert legend.get_title().get_text() == 'Genre', f'Expected legend title "Genre", but got {legend.get_title().get_text()}'
        assert legend.get_bbox_to_anchor()._bbox.x0 == 1 and legend.get_bbox_to_anchor()._bbox.y0 == 0.5, f'Expected legend location (1, 0.5), but got ({legend.get_bbox_to_anchor()._bbox.x0}, {legend.get_bbox_to_anchor()._bbox.y0})'
        loc = legend._loc
        assert loc == 7, f'Expected legend location "center right" (7), but got {loc}'
