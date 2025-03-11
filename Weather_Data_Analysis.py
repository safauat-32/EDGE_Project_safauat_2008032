# -*- coding: utf-8 -*-
"""Data Frame Basics

1.   Creating Dataframe
2.   Dealing with rows and columns
3.   Operations - min, max, mean, std, describe
4. Conditional selection
5. Set Index
"""

import pandas as pd

df = pd.read_csv('1901_2019_BD_weather.csv')

df

rows, columns = df.shape
rows

df.head(5)

df.tail(5)

df[2:5]

df[:]

df.columns

df['Month'] #or df.month

type(df['Month'])

df[['Year','Rain']]

df['Rain'].max()

df['Rain'].mean()

df['Rain'].min()

df['Rain'].std()

df.describe()

df[df.Rain <=40]

df[df.Rain == df.Rain.max()]

df[['Year','Month']][df.Rain == df.Rain.max()]

df.set_index('Year', inplace=True)

df

df.loc[2019]

df.reset_index(inplace=True)
"""
Different types of creating DataFrame

1.   Using CSV file
2. From python dictonary
3. From list of tuples
4. From list of dictonaries


"""

import pandas as pd
df = pd.read_csv("weather.csv")
df

#with pyhton dictonary

weather_data = {
    'day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'temp': [12, 14, 15, 18, 20, 22, 24],
    'windspeed': [6, 7, 8, 9, 10, 11, 12],
    'event': ['Rain', 'Sunny', 'Snow', 'Rain', 'Sunny', 'Snow', 'Rain']
}
df = pd.DataFrame(weather_data)
df

#using a tuples list
weather_data = [
    ('Monday', 12, 6, 'Rain'),
    ('Tuesday', 14, 7, 'Sunny'),
    ('Wednesday', 1)
]
df = pd.DataFrame(weather_data, columns=['day', 'temp', 'windspeed', 'event'])
df

#list of disctonaries
weather_data = [
    {'day': 'Monday', 'temp': 12, 'windspeed': 6, 'event': 'Rain'},
    {'day': 'Tuesday', 'temp': 14, 'windspeed':5, 'event': 'Sunny'},
    {'day': 'Wednesday', 'windspeed':4, 'event': 'Snow'},
]
df = pd.DataFrame(weather_data)
df
