import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import csv

df = pd.read_csv("data.csv")

fig = ff.create_distplot([df["Height(Inches)"].tolist()], ["Height"], show_hist=False)

fig.show()