import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

# CLEANING & SET UP:

# reading steel price data
df = pd.read_csv("STEEL_PRICE.csv")
print(df.head())
print(df.info())

# convert DATE column to datetime format
df["DATE"] = pd.to_datetime(df["DATE"])

# set Jan 2015 as a 'baseline' value
baseline = df.loc[df["DATE"] == "2015-01-01", "VALUE"].iloc[0]
print(baseline)

# rebase values relative to jan 2015
df["VALUE_2015_BASE"] = (df["VALUE"] / baseline) * 100
# round to nearest tenth
df["VALUE_2015_BASE"] = df["VALUE_2015_BASE"].round(1)

# save new rebased csv file
df.to_csv("STEEL_PRICE_rebased.csv", index=False)



# CONDUCTING DiD:

# 0 before March 2018, 1 from March 2018 onward
df["tariff_post"] = (df["DATE"] >= "2018-03-01").astype(int)

# add linear month trend
df["month_index"] = range(len(df))

# run regression of pre/post with trend
model = smf.ols("VALUE_2015_BASE ~ tariff_post + month_index", data=df).fit()
print(model.summary())

# plot steel prices with tariff introduction
plt.figure(figsize=(10,5))
plt.plot(df["DATE"], df["VALUE_2015_BASE"], label="Steel Price Index (Jan 2015=100)")
plt.axvline(pd.to_datetime("2018-03-01"), color="red", linestyle="--", label="Tariff Introduced")
plt.xlabel("Date")
plt.ylabel("Steel Price Index")
plt.title("Steel Prices (2015–2019) with Tariff Introduction")
plt.legend()
plt.show()