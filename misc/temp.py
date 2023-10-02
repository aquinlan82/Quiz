import pandas as pd
import wikipedia

text = wikipedia.page(wikipedia.random()).content
sentences = text.replace("\n","").split(".")
for s in sentences:
    print(s)
    print("\n\n")

# wiki_wiki = wikipediaapi.Wikipedia('MyProjectName (merlin@example.com)', 'en')
# page_py = wiki_wiki.page('https://en.wikipedia.org/wiki/Special:Random')

# print(page_py.text)


# df = pd.read_csv("data/Territory Flags/data.csv")

# # rest = df[df["Continents"] != "Africa"]
# # adf = df[df["Continents"] == "Africa"]
# # adf["Axis 1"] = adf["Axis 1"].str[:-4] + ".jpg"

# # df = pd.concat([rest,adf])

# # print(df)

# df["Axis 1"] = df["Axis 2"] + ".png"


# df.to_csv("data.csv")