import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as pp

planets = pd.read_csv("./chapter2/02_03/Planets.csv")
planets.head()
planets.describe()
planets["Mass"]

# Look at first
planets.loc[0]

# Set the index
planets.set_index("Planet", inplace=True)

# Presents information about the dataframe
planets.info()

planets.loc["MERCURY"]

# .loc accepts ranges (and are inclusive)
planets.loc["MERCURY": "EARTH"]

planets.FirstVisited["MERCURY"]

planets.loc["MERCURY"].FirstVisited

planets.loc["MERCURY", "FirstVisited"]

type(planets.loc["MERCURY", "FirstVisited"])

# Assign the FirstVisited series to now be the datetime version of the string data
planets.FirstVisited = pd.to_datetime(planets.FirstVisited)

# the .dt property exists on all datetimes
planets.FirstVisited.dt.year
planets.FirstVisited.dt.month

# How long has it been since 2019 that each planet was visited?
2019 - planets.FirstVisited.dt.year

# planets.loc["MARS"].FirstVisited.month - planets.loc["MOON"].FirstVisited.month
delta = planets.FirstVisited["MARS"] - planets.FirstVisited["MOON"]
years_between_mars_and_moon_landing = delta / np.timedelta64(1, 'Y')
months_between_mars_and_moon_landing = delta / np.timedelta64(1, 'M')
