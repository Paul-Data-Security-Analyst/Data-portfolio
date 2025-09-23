#importing libraries
import pandas as pd

# #creating DATAFRAME from dataset
# df = pd.read_csv("data/netflix_titles.csv")
# # displaying the overall information about the Dataset
# print("\n---DATA INFO---with 'NONE'\n")
# print(df.info())
# print("\n---INFO---without 'NONE'---\n")
# df.info()
# # displaying the Number of Rows & Columns
# print("\n---SHAPE---\n")
# print(df.shape)
# # displaying 5 random rows from dataset
# print("\n---SAMPLE 5 ROWS---\n")
# print(df.sample(5))
# # displaying head & Tail
# print("\n---HEAD & TAIL---\n")
# print(df.head(3))
# print(df.tail(2))
# # describing the numeric statistics of a dataframe
# print("\n---Numeric value Description---\n")
# print(df.describe())
# # printing Datatypes from DataFrame
# print("\n---DATA TYPES---\n")
# print(df.dtypes)

# Detecting Missing Values
df_demo = pd.DataFrame({ "Title":["Harry Potter","Megatronn","jaws",None],"release year" :["2000",None,None,"2021"],"Artist": ["Jim Tim", "Daniel",None,"DSP"]})
# printing Missing values and the count
print("\n---MISSING VALUE---\n")
print(df_demo.isna())
print("\n---MISSING VALUES COUNT---\n")
print(df_demo.isna().sum())
print("\n---MISSING VALUES COUNT ROUNDED OFF---\n")
print((df_demo.isna().mean() * 100).round(1))

# Dropping missing values
print("\n---Dropped Rows---\n")
print(df_demo.dropna())
print("\n---Dropped columns---\n")
print(df_demo.dropna(axis=1))
print("\n---Dropped Rows with all NONE values---\n")
df_col_all_none_values = df_demo.dropna(how="all")
print(df_col_all_none_values)
print("\n---Dropped Rows with columns specified---\n")
print(df_demo.dropna(subset=["release year"]))

# Always copy before filling values
df_demo.copy()
# Filling missing values
print("\n---FILLING ALL MISSING VALUES---\n")
df_filled = df_demo.fillna("**star**")
print(df_filled)
print("\n---FILLING COLUMNWISE VALUES (TITLE) ---\n")
print(df_demo["Title"].fillna("**MOVIE**"))
print("\n---FILLING COLUMNWISE VALUES (release year) ---\n")
print(df_demo["release year"].fillna("**YEAR**"))
print("\n---FILLING COLUMNWISE VALUES (Artist) ---\n")
print(df_demo["Artist"].fillna("**AUTHOR**"))

# Checking for Missing values

print("\n---CHECKING FOR MISSING VALUES---\n")
print(df_filled.isna().sum())
print("\n---CHECKING for missing values from COUNTS using conditionals---\n")
df_count = df_filled.isna().sum()
print("COUNT")
print(df_count)
if df_count.sum() ==0:
    print("---\nNo Missing Values\n---")
else:
    print("---\nstill missing values\n---")






