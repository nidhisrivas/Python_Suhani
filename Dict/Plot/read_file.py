import pandas as pd



csvFile = "C:\\Users\\nidhi\\OneDrive\\Documents\\GitHub\\Python\\Dict\\Plot\\Dataset.csv"
colName = "Height"

df = pd.read_csv(csvFile)
column_list = df[colName].tolist()

print(column_list)



