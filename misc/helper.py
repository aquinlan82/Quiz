import pandas as pd
import os

# dir_list = os.listdir("data/President Years/images")
# df = pd.DataFrame(dir_list)


df = pd.read_csv("data/President Years/data.csv")
df["Axis 1"] = df["From"].map(str) + "-" + df["To"]

df.to_csv("temp.csv")
