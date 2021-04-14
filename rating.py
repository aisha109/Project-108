
import pandas as pd 
import plotly.figure_factory as ff 
import csv

data = pd.read_csv("data.csv")

fig = ff.create_distplot([data['Avg Rating'].tolist()], ["Average Ratings"])
fig.show()