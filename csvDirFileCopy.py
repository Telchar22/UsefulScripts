import os
import shutil
import csv
# r"G:\X-ray\data\Data_Entry_2017.csv"

# Open a file
path = r"G:\X-ray\data\images"
destination = r"G:\X-ray\data\learning"
dirs = os.listdir(path)

with open("Data_Entry_2017.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
    images = list(reader)
    for row in images:
        n = os.path.join(path, row[0])
        shutil.copy(n, destination)
