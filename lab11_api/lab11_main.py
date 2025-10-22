"""
Tommy Garrido
Oct 22, 2025
Lab 11, APIs
"""
import pandas as pd


# -----------
# 1. Example dataframe
# -----------
dict_ = {
    'a':[11,21,31],
    'b':[12,22,32]
}

# create a dataframe for dict_

df = pd.Dataframe(dict_)

# display the firt few rows of the dataframe
df.head()
