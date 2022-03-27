#%%
import pandas as pd
import altair as alt
import numpy as np

mpg_data = pd.read_csv('mpg.csv')

# Chart

chart = (alt.Chart(mpg_data)
    .encode(
        x="displ",
        y="hwy",)
        .mark_circle()
)

chart.save("project0_chart.png")


# %%


print(mpg_data
    .head(5)
    .filter(["manufacturer", "model","year", "hwy"])
    .to_markdown(index=False))






# %%
