import pandas as pd

tabel_data = pd.read_csv('data.csv') # Be sure you have the data.csv file in the same directory
print(f"{tabel_data} \n")
print(tabel_data.head()) # Shows only the first 5 rows

# Uncomment one or more of the functions if you want to try more PANDAS library functions
# print(tabel_data.info())
# print(tabel_data.describe())
# print(tabel_data.columns)
# print(tabel_data.shape)
# print(tabel_data.size)
# print(tabel_data.dtypes)
# print(tabel_data.isnull().sum())
# print(tabel_data.dropna())
# print(tabel_data.drop_duplicates())