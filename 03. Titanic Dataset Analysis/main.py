import pandas as pd 

df = pd.read_csv("titanic.csv")

# print(df)
# print(df["Age"])
print(df[["Age","Cabin"]])

# print(df.to_string())


# Data Inspection

first_top_5 = df.head()
print(first_top_5)

# print(df.describe())


#Data Cleaning.
# Way 1 
# df["Age"] = df["Age"].fillna(df["Age"].median())

#Way 2 (Pandas recommendation way)
df.fillna({"Age":df["Age"].median()}, inplace=True)

# print(df["Age"])


df.drop(columns=["Cabin","Ticket"],inplace=True)

# print(df)


# EDA

# print(df.groupby("Pclass")["Survived"].mean())