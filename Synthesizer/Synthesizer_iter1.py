# Machine Learning Team
# Mohammad Firas Sada (msada@hawk.iit.edu)
# Arjun Aggarwal (arjuna4@illinois.edu)
# Lauren-Charlise Walls (lwalls4@uic.edu)
# September 16, 2022

#!/usr/bin/python

import sys
import csv
import os
import pandas as pd
import numpy as np


def writeNoise(f,reader,df,lowNoise, highNoise,cur_stp,stp):
    writer = csv.writer(f)
    writer.writerow(next(reader))
    for row in reader:
        syn_row = [cur_stp] + [float(item) + np.random.normal(lowNoise,highNoise) for item in row[1:13]]
        writer.writerow(syn_row)
        cur_stp+=stp
    return cur_stp

def writeToCSV(reader_str, num , lowNoise, highNoise,df):
    mx,min=df['Time'].max(),df['Time'].min()
    stp = (mx-min)/sum(1 for line in df)
    cur_stp = mx+stp
    for i in range(num):
        reader = csv.reader(open(reader_str), delimiter="\t")
        outputFileName = "output #.csv"
        outputVersion = 1
        while os.path.isfile(outputFileName.replace("#", str(outputVersion))):
            outputVersion += 1
        outputFileName = outputFileName.replace("#", str(outputVersion))
        with open(outputFileName, 'w', newline='', encoding='UTF8') as f:
            cur_stp = writeNoise(f, reader,df, lowNoise, highNoise,cur_stp,stp)
            # writer = csv.writer(f)
            # for row in reader:
            #     writer.writerow(reader)

def parseParameters(x):
    if (len(x) != 3):
        raise Exception("Incorrect Number of Parameters")
    try:
        reader = csv.reader(open(x[0]), delimiter="\t")
        df=pd.read_csv(x[0],sep='\t')
        file_name = x[0]
    except:
        raise Exception("Incorrect File Name")
    try:
        num = int(x[1])
    except:
        raise Exception("Incorrent Number Format")
    lowNoise, highNoise = 0,0
    try:
        noise = x[2].split(',')
        lowNoise,  highNoise = float(noise[0]), float(noise[-1])
    except:
        raise Exception("Incorrect Gaussian Bounds. Please try x-y where x is low and y is high.")
    return file_name, num , lowNoise, highNoise,df

def main(list):
    #file_name, output_num , noise_bounds = parseParameters(list[1::]) 
    writeToCSV(*parseParameters(list[1::]))

main(sys.argv)
