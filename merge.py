import pandas as pd

data_2015 = pd.read_csv('./data/2015.csv')
data_2016 = pd.read_csv('./data/2016.csv')
data_2017 = pd.read_csv('./data/2017.csv')
data_2018 = pd.read_csv('./data/2018.csv')

combined_data = pd.concat([data_2015, data_2016, data_2017, data_2018], ignore_index=True)

combined_data.to_csv('combined_data.csv', index=False)
