import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as pp

# To figure out the type, run `!file billboard.csv` in ipython

# specify the encoding of the file
billboard = pd.read_csv("./chapter2/02_04/billboard.csv", encoding = "latin-1")
billboard.head()

billboard.columns

pp.plot(billboard.loc[0,'x1st.week': 'x76th.week'])

# dataframe.iterrows() is the iterable of the dataframe
for index, row in billboard.iterrows():
    pp.plot(range(1, 77), row["x1st.week": 'x76th.week'], color='C0', alpha=0.1)

# Let's get to cleaning b/c the rankings are divided over many columns
# Make each ranking in a separate row with a week# as a variable (called melting)
bshort = billboard[["artist.inverted", "track", "time", "date.entered", "x1st.week", "x2nd.week", "x3rd.week"]]
bshort.head()
bshort.columns = ["artist", "track", "time", "date.entered", "wk1", "wk2", "wk3"]

bmelt = bshort.melt(['artist', 'track', 'time', 'date.entered'], ['wk1', 'wk2', 'wk3'], 'week', 'rank')
bmelt

billboard.head()
melt = billboard.melt(["artist.inverted", "track", "time", "genre", 'date.entered', 'date.peaked'], ["x1st.week", "x76th.week"], 'week', 'rank')
melt.week = melt.week.str.extract('(\d+)')
melt = melt.rename(columns={"artist.inverted": "artist"})
melt.head()
melt.tail()

# Query takes a query as a string
melt.query('track == "Liar"')

# Convert the week field into an integer
melt.week = pd.to_numeric(melt.week)

melt["date.entered"] = pd.to_datetime(melt["date.entered"])
melt["date.peaked"] = pd.to_datetime(melt["date.peaked"])

melt["date"] = melt["date.entered"][0] + pd.Timedelta("7 days") * (melt["week"] - 1)
melt = melt.drop(['date.entered'], axis=1)
melt.head()

# Short the columns and the rows
billboard_final = melt[["artist", "track", "time", "date", "week", "rank"]]
billboard_final.sort_values(["artist", "track"], inplace=True)

# Remove duplication by normalizing
tracks = billboard_final[["artist", "track", "time"]].drop_duplicates()
tracks.index.name = "id"
tracks = tracks.reset_index()
tracks.head()

# Join the dataframes back together
tidy = pd.merge(tracks, billboard_final, on=["track", "artist", "time"]).drop(["artist", "track", "time"], axis=1)
tidy.head()

## 
tidy.loc[tidy[tidy.week == 1]["rank"].index]
tracks.query('id == 1')