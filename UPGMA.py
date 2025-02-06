import pandas as pd

data = {
    "A": [0, 19, 27, 8, 33, 18, 13],
    "B": [19, 0, 31, 18, 36, 1, 13],
    "C": [27, 31, 0, 26, 41, 32, 29],
    "D": [8, 18, 26, 0, 31, 17, 14],
    "E": [33, 36, 41, 31, 0, 35, 28],
    "F": [18, 1, 32, 17, 35, 0, 12],
    "G": [13, 13, 29, 14, 28, 12, 0],
}

table = pd.DataFrame(data, index=["A", "B", "C", "D", "E", "F", "G"])

print(table)