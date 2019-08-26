import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as pp

final = pd.read_csv("./chapter2/02_05/final.csv")
final.head()

df = pd.read_csv("./chapter2/02_05/tb.csv")
df.head()
df.columns

melted = df.melt(["country", "year"], ["m04", "fu"], "sexage", "cases")
melted.head()

melted["sex"] = melted["sexage"].str.slice(0,1)
melted["age"] = melted["sexage"].str.slice(1)
melted.head()
melted["age"] = melted["age"].map({
    "04": "0-4",
    "515": "5-14",
    "1524": "15-24",
    "2534": "25-34",
    "3544": "34-44",
    "4554": "45-54",
    "5564": "55-64",
    "65": "65+",
    "u": np.nan
})
melted.head()

# Drop all the unknown values
final = melted.dropna(subset=["cases"])
final.sort_values(["country", "year", "age", "sex"])
final = final[["country", "year", 'age', 'sex', 'cases']]
final.head()