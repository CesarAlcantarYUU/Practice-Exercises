#importing pandas and numpy libaries and assigning alias of pd and np
import pandas as pd
import numpy as np

# creating a series list with assigned variable "data"
data = pd.Series([10, 20, 30, 20, np.nan])

print(data)

#printing the sum, mean. maximum, and minimum
print("Sum:", data.sum())
print("Mean:", data.mean())
print("Maximum:", data.max())
print("Minimum:", data.min())

# shows only first 3 values
print(data.head(3))

# identifying missing values
print("Missing Values:")
print(data.isnull())

# replacing missing values with 0
print("Replace missing values with 0:")
print(data.fillna(0))

# sorting the series values
print("Sorted Values:")
print(data.sort_values())

## counting repeated values in the series
print("Repeated Values:")
print(data.value_counts())