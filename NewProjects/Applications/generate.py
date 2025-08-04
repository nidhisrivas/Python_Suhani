#!/usr/bin/python

# A Python program to read a csv and write print out few coloumns from it
# Author: Suhani Khare


## Read_A_csv

## Generate_column

import os
import csv
import json
import pandas as pd
from pprint import pprint


def generate_coloumns():
    '''A module to read a csv file and selecting columns'''

    print("Generating Columns ...Hang in there\n")

    # time.sleep(4)
    col_list = ["First_Name", "Last_Name", "Age", "Gender",
                "Occupation", "City", "State", "Country", "Employer"]
    

    try:
        # Default encoding is 'utf-8' which wasn't working before
        data = pd.read_csv(
            "Data/information.csv", encoding="iso-8859-1", usecols=col_list)
        csv_df = pd.DataFrame(data)
        print(f"Printing Coloumns\n")
        # print(data)
        print(csv_df)
        # return (csv_df)
        return (csv_df)

    except Exception as e:
        print(f"This is the error {e}")


def write_to_file(df):

   ''' A Module to get the write the selected columns into another csv '''
   print(f"Writting to another csv")
   file_w = open('Reports/updated.csv','w',newline="")
   with file_w:
      header = ["F_Name","L_Name","Age","Gender"]
      writer = csv.DictWriter(file_w,fieldnames=header)
      writer.writeheader()
      
      print(f"Total number of rows in csv file is {len(df)}\n")
   
      ### Reading the df values and saving it in a variable
      for i in range(len(df)):
        F_Name = df["First_Name"][i]
        L_Name = df["Last_Name"][i]
        Age = df["Age"][i]
        Gender = df["Gender"][i]
    
      ### Preparing a dictionary to write it to csv
        info = {"F_Name":F_Name,
              "L_Name":L_Name,
               "Age":Age,
               "Gender":Gender
              }

      ## Writting to CSV
        writer.writerow(info)
       
    



### --- Main_Function ---###

# Get the columns from CSV
df = generate_coloumns()

write_to_file(df)

