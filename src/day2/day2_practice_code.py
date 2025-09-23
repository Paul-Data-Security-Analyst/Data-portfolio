#importing libraries
import pandas as pd

#creating DATAFRAME from dataset
df = pd.read_csv("data/netflix_titles.csv")
# displaying the overall information about the Dataset
print("\n---DATA INFO---with 'NONE'\n")
print(df.info())
print("\n---INFO---without 'NONE'---\n")
df.info()
# displaying the Number of Rows & Columns
print("\n---SHAPE---\n")
print(df.shape)
# displaying 5 random rows from dataset
print("\n---SAMPLE 5 ROWS---\n")
print(df.sample(5))
# displaying head & Tail
print("\n---HEAD & TAIL---\n")
print(df.head(3))
print(df.tail(2))
# describing the numeric statistics of a dataframe
print("\n---Numeric value Description---\n")
print(df.describe())
# printing Datatypes from DataFrame
print("\n---DATA TYPES---\n")
print(df.dtypes)


