"""
Data gen module contains essential tools to gennerate
data to csv format.
"""

import csv

def get_csv(rows, features={}, to_path="gen.csv"):
    """
    According to features the data are generated to the 
    specified path
    """
    cols = len(features.keys())
    if not cols:
        return

    datas = [["ok" for i in range(cols)] for j in range(rows)]

    with open(to_path, "w", encoding='UTF8' , newline='') as f:
        writer = csv.writer(f)
        writer.writerow(features.keys())

        writer.writerows(datas)
