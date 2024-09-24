import unittest
import matplotlib.pyplot as plt
from tests import TestChartSettings

"""
Write your code here. Solve the task from .md file by setting figure and axes up
"""

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 2, 3], label='test')

suite = unittest.TestSuite()
suite.addTest(TestChartSettings('test_figsize', fig=fig, ax=ax))
suite.addTest(TestChartSettings('test_xlabel', fig=fig, ax=ax))
suite.addTest(TestChartSettings('test_ylabel', fig=fig, ax=ax))
suite.addTest(TestChartSettings('test_title', fig=fig, ax=ax))
suite.addTest(TestChartSettings('test_legend_exists', fig=fig, ax=ax))
suite.addTest(TestChartSettings('test_legend_title', fig=fig, ax=ax))
suite.addTest(TestChartSettings('test_legend_location', fig=fig, ax=ax))
suite.addTest(TestChartSettings('test_legend_loc', fig=fig, ax=ax))

runner = unittest.TextTestRunner()
runner.run(suite)