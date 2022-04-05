import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_excel("HealthInformaticsProject.xlsx", sheet_name="DataFinal")

print(data.columns)

contigency= pd.crosstab(data["Worked Out"],data['Calories'],normalize='index')

# data['Github contributions'],data['Sum of Hours and Minutes Phone Usage'],data['Sum of Hours and Minutes Social Phone Usage']

# df_gh_con = data.pivot(index='Date', columns='Worked Out', values='Github contributions')

# df_cal = data.pivot(index='Date', columns='Worked Out', values='Calories')

# print(df_cal)

# for i in df_cal:
#     df_cal[i]