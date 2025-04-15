# messingwithpandas.py
# Author: Zoe McNamara Harlowe

import pandas as pd
import csv

list_of_lists = [
    ["John",     "Maths",    23],
    ["Mary",    "English",  52],
    ["Joe",     "History",  91],
    ["Zoe",     "Biology",  45],
    ["Tom",     "Maths",    67],
    ["Jerry",   "English",  89],
    ["Mickey",  "History",  34],
    ["Donald",  "Biology",  76]
]

df = pd.DataFrame(list_of_lists, columns=["Name", "Subject", "Score"])
print(df.describe())
print(type(df))

FILENAME = "grades.csv"

with open(FILENAME, 'w') as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(["Name", "Subject", "Score"])
    writer.writerows(list_of_lists)

path = "week10"

excel_filename = path +'grades.xlsx' 
df.to_excel(excel_filename, index=False, sheet_name='data')

with pd.ExcelWriter(excel_filename, engine='openpyxl', mode='a') as writer: 
    df.describe().to_excel(writer, sheet_name="summary") 
