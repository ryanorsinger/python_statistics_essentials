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
melt = billboard.melt(["artist.inverted", "track", "time", "genre"], ["x1st.week", "x76th.week"], 'week', 'rank')
melt.head()