import csv 
import random
import math
import numpy as np

def loadDataset(filename):
    with open(filename,'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        headders = dataset[0]
        dataset = dataset[1:len(dataset)]
        return dataset , headders
dataset , headers = loadDataset('Real esate.csv')
print("HEADERS")
print(headers)           
