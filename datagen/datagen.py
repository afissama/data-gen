"""
Data gen module contains essential tools to gennerate
data to csv format.
"""
import csv
import random
import numpy


def get_csv(rows, features={}, to_path="gen.csv"):
    """
    According to features the data are generated to the 
    specified path
    """
    cols = len(features.keys())
    if not cols:
        return

    datas = [[] for j in range(cols)]

    idx = 0
    for j in features.keys():
        datas[idx] = __random_gen(rows, features[j])
        idx = idx +1

    datas = numpy.transpose(datas)

    with open(to_path, "w", encoding='UTF8' , newline='') as f:
        writer = csv.writer(f)
        writer.writerow(features.keys())

        writer.writerows(datas)


def __random_gen(rows, feat):
    """
    Generate randomly data for column and return array
    """
    datas = ["" for j in range(rows)]
    idx = 0
    i = 0

    for key in feat.keys():
        for i in range(idx , idx + 1 + feat[key]):
            if i < rows:
                datas[i] = key
        idx = i
    random.shuffle(datas)
    return datas
