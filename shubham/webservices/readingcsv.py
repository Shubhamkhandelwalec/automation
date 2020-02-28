# Load the Pandas libraries with alias 'pd'
import pandas as pd
# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later)
data = pd.read_csv("Pet Breeds - Sheet1 resend.csv",usecols=[0])


for j in data:
    print(">>>>>>",j)
for i in data.index:
    if str(data['Feline'][i]) == 'nan':
        continue
    print(data['Feline'][i])

