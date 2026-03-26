import pandas as pd

# marks = pd.Series([1,2,34], index=["Ram","Shyam","Prabin"])


marks = pd.Series([1,2,34],
                  index=["Ram","Shyam","Prabin"])

# print(marks.dtype)
# print(marks.info())
# print(marks.describe())
# print(marks.loc["Ram"])
# print(marks.iloc[0])
# print(marks.head(1))
# print(marks.tail(1))
# print(marks.isnull())

# filtering.
print(marks[marks > 5])