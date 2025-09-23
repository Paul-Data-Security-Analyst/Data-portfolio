#importing library
import pandas as pd
#user-defined data
data = { "Title":['Genesis','Exodus','Luke','John'],
         "Released": ["BC 45","BC 48","AD 45","AD 49"],
         "Author": ["Moses","Moses","Luke","Moses"],
         "year":["2021","2021","2024","2023"]}

#converting into Dataframe
df = pd.DataFrame(data)
print("---DATA FRAME---")

#printing the DataFrame
print(df)

#inspecting the DataFrame
print("\n---SHAPE---\n",df.shape)

#printing head(argument) values
print("\n---FIRST 3 HEAD VALUES(3)---\n",df.head(3))

#Filtering in DataFrames
print("\n---Filter AUTHOR---\n")
df_Moses = df[df["Author"]=="Moses"]
print(df_Moses)

print("\n---Filter YEAR---\n")
df_year = df[df["year"]=="2021"]
print(df_year)

#Finding Range
print("\n---EARLIEST RELEASE YEAR---\n")
print(df["Released"].min())

print("\n---LATEST RELEASE YEAR---\n")
print(df["Released"].max())






