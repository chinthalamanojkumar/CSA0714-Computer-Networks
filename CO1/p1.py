import pandas as pd

data = {
    "Name": ["Ram", "Ravi", "Sita"],
    "Age": [20, 21, 22]
}

df = pd.DataFrame(data)
print(df)


import pandas as pd

data = {
    "Name": ["Ram", "Ravi", "Sita", "Raju", "Kiran", "Anu"],
    "Age": [20, 21, 22, 23, 24, 25]
}

df = pd.DataFrame(data)
print(df.head())

import pandas as pd

data = {
    "Name": ["Ram", "Ravi"],
    "Age": [20, 21]
}

df = pd.DataFrame(data)
print(df.columns)

import pandas as pd

data = {
    "Name": ["Ram", "Ravi"],
    "Age": [20, 21]
}

df = pd.DataFrame(data)
print(df.dtypes)

import pandas as pd

data = {
    "Age": [20, 21, 22, 23, 24]
}

df = pd.DataFrame(data)
print(df.describe())