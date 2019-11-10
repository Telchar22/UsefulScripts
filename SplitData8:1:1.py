import os
import shutil
import csv
from random import randint

path = r"G:\no finding"
#CardiomegalyTrain.csv
#FindingTrainData.csv

with open("FindingTrainData.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
    images = list(reader)
    for row in images:
        n = os.path.join(path, row[0])
        #shutil.copy(n, destination)
        r = randint(0, 9)
        if r < 8:
            shutil.move(n, r"G:\no finding\train")
        elif r == 9:
            shutil.move(n, r"G:\no finding\test")
        else:
            shutil.move(n, r"G:\no finding\valid")
