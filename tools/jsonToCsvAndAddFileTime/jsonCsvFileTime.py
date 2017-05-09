#! /usr/bin/python
__author__ = 'RoGeorge'

import os
import datetime
import json
import csv
import sys
from collections import OrderedDict
from time import *

# for each JSON file
path = './jsonFilesOnly/'
row = OrderedDict()

for fileName in os.listdir(path):

    fileTime = os.path.getmtime(path + fileName)
    fileTime = datetime.datetime.fromtimestamp(fileTime)
    strFileTime = fileTime.strftime("%Y-%m-%d %H:%M:%S")
    # strftime("%Y-%m-%d_%H.%M.%S", fileTime)

    f = open(path + fileName)
    data = json.load(f)
    f.close()

    with open('out.csv', 'a') as csvFile:

        # writer = csv.writer(csvFile, delimiter='\t')

        for row in data:

            line = row["name"].encode('utf-8') + '\t' + \
                   str(row["count"]) + '\t' + \
                   str(row["id"]) + '\t' + \
                   str(row["award"]) + '\t' + \
                   strFileTime + '\n'

            csvFile.write(line)

    csvFile.close()
