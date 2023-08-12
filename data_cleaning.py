# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 15:11:51 2023

@author: Dell

"""

import pandas as pd

path = "C:/Users/Dell/Documents/US_DATASCIENCE_SALARY_PROJ/US_Data_Science_Jobs.xlsx"


import pandas as pd

path = "C:/Users/Dell/Documents/US_DATASCIENCE_SALARY_PROJ/US_Data_Science_Jobs.xlsx"


df = pd.read_excel(path)

df = df[df['salary_avg'] != 0]

#Limiting salary pay period to annual
df = df[df['salary_payPeriod'] == 'ANNUAL']

#limiting salary source to estimated
df = df[df['salary_source'] == 'ESTIMATED']

#age of company
df['age'] = df.yearFounded.apply(lambda x: x if x <1 else 2023 - x)
df = df[df['yearFounded'] != 0
        ]