import pandas as pd


df = pd.read_csv("data/Territory Flags/data.csv")

# rest = df[df["Continents"] != "Africa"]
# adf = df[df["Continents"] == "Africa"]
# adf["Axis 1"] = adf["Axis 1"].str[:-4] + ".jpg"

# df = pd.concat([rest,adf])

# print(df)

df["Axis 1"] = df["Axis 2"] + ".png"


df.to_csv("data.csv")