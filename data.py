import random 
import plotly.express as px
import pandas as pd 
import csv 
data=pd.read_csv("data.csv")
mean=data.groupby(["Avg Rating", "Mobile Brand"])["Sr.No"].mean()
fig=px.scatter(mean, x="Mobile Brand", y="Avg Rating", size="Sr.No")
fig.show()
