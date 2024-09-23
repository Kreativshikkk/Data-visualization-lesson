# Data visualization lesson

## Why we use charts

Charts and graphs are essential tools in data visualization. They allow us to present complex data in an easily understandable format, helping to uncover patterns, trends, and outliers. Instead of sifting through rows of raw data, charts offer a visual summary, making it easier to interpret and communicate insights.

Graphs can reveal:
1. **Trends over time** (e.g., sales growth over months)
2. **Comparisons** (e.g., performance of different products or platforms).
3. **Distributions** (e.g., frequency of game genres).

and etc

## Basic Principles for Creating Effective Graphs

Before jumping into creating a chart, it’s important to follow some basic rules to ensure your graph is both accurate and visually clear:

1. **Keep it simple**: A clear, minimalistic chart can convey the message better
2. **Label axes clearly**: Ensure that both the X and Y axes are labeled so viewers know what each axis represents
3. **Use appropriate scales**: Avoid distorting the scale to exaggerate or minimize trends
4. **Use colors wisely**: Differentiate categories or series with distinct colors but avoid using too many colors, as that can make the chart confusing
5. **Add legends**: For charts comparing multiple variables, a legend helps in distinguishing between them

## Single Bar Chart

In this lesson we will create single bar chart showing the number of games for `4` popular gaming platforms (PS4, XOne, PC and WiiU) broken down by game genre. We'll be working with Python and using this [dataset](https://drive.google.com/file/d/1Cw2wO3lHHJ13B1w4p-FgX1SHVtlUtfga/view?usp=drive_link).

Here is the example of the final chart:

![example](https://github.com/user-attachments/assets/f0b0ae5a-f0bb-42f3-badc-8554ad6bdbe3)
<p align="center">
</p>

Let’s dive into the process of creating this chart step by step.

## Required libraries

To build this visualization, you will need the following Python libraries:
- `matplotlib` – for plotting charts
- `numpy` – for data manipulation
- `pandas` – for handling the dataset

If you are using PyCharm, these libraries can be easily installed via the **Python Packages** tool. Alternatively, use the following commands in your terminal:

```bash
pip install matplotlib numpy pandas
```

## Lesson outline

The entire lesson is divided into 6 steps which should be completed in this order:
1. **Import dataset**:  Load the data into a Pandas DataFrame
2. **Create an empty chart**: Set up a basic chart with axis titles and a legend
3. **Extract necessary data**: Filter the dataset for the platforms and genres we’re interested in
4. **Plot data for one platform**: Start with one platform
5. **Plot all platforms**: Add data for the other platforms
6. **Stylize the chart**: Enhance the appearance of the chart

Ready to get started? Let’s go!
