# Machine Learning Team
# Mohammad Firas Sada (msada@hawk.iit.edu)
# Arjun Aggarwal (arjuna4@illinois.edu)
# Lauren-Charlise Walls (lwalls4@uic.edu)
# September 16, 2022

#!/usr/bin/python

import sys
import csv
import os
import numpy as np

# parameters are a list called: sys.argv

def writeToCSV(data):
    outputFileName = "output #.csv"
    outputVersion = 1
    while os.path.isfile(outputFileName.replace("#", str(outputVersion))):
        outputVersion += 1
    outputFileName = outputFileName.replace("#", str(outputVersion))
    with open(outputFileName, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)

def parseParameters(x):
    if (len(x) < 4 or len(x) > 5):
        raise Exception("Incorrect Number of Parameters")
    try:
        time = float(x[0])
    except:
        raise Exception("Incorrect Time Format")
    try:
        step = float(x[1])
    except:
        raise Exception("Incorrent Step Format")
    try:
        rows = int(x[2])
    except:
        raise Exception("Incorrent Row Count Format")
    try:
        bounds = x[3].split(',')
        low = float(bounds[0])
        high = float(bounds[-1])
    except:
        raise Exception("Incorrect Bounds. Please try x-y where x is low and y is high.")
    lowNoise, highNoise = 0,0
    if (len(x) == 5):
        try:
            noise = x[4].split(',')
            lowNoise,  highNoise = float(noise[0]), float(noise[-1])
        except:
            raise Exception("Incorrect Gaussian Bounds. Please try x-y where x is low and y is high.")
    dataset = [['Time']+['Channel ' + str(i) for i in range(12)]]
    for i in range(int(rows)):
        row = [time + (step*i)] + [np.random.uniform(low,high) + np.random.normal(lowNoise,highNoise) for x in range(12)]
        dataset.append(row)
    return dataset

def main(list):
    dataset = parseParameters(list[1::])
    writeToCSV(dataset)

main(sys.argv)
