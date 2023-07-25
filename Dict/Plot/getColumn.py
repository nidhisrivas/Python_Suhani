
import pandas as pd

def getCol(csvFile, colName):
    print(csvFile)
    df = pd.read_csv(csvFile)
    column_list = df[colName].tolist()
    return column_list

