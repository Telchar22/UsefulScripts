import os, sys
import shutil
import csv
from random import randint
from PIL import Image
path = r"G:\PROJEKT\data\data\images"

i = 0
with open("CardiomegalyTrain.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
    images = list(reader)
    
    for row in images:
        n = os.path.join(path, row[0])
        r = randint(0, 9)
        if r < 8:
            shutil.copy(n, "G:/PROJEKT/INZPROJ/data/train/cardiomegaly")
        else:
            shutil.copy(n, "G:/PROJEKT/INZPROJ/data/valid/cardiomegaly")

with open("NoFindingTrain.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
    images = list(reader)

    for row in images:
        n = os.path.join(path, row[0])
        if i % 22 == 0:
            r = randint(0, 9)
            if r < 8:
                shutil.copy(n, "G:/PROJEKT/INZPROJ/data/train/nofindings")
            else:
                shutil.copy(n, "G:/PROJEKT/INZPROJ/data/valid/nofindings")
        i += 1

with open("NoFindingTest.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
    images = list(reader)

    for row in images:
        n = os.path.join(path, row[0])
        shutil.copy(n, "G:/PROJEKT/INZPROJ/data/test/nofindings")

with open("cardiomegaliaTest.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
    images = list(reader)

    for row in images:
        n = os.path.join(path, row[0])
        shutil.copy(n, "G:/PROJEKT/INZPROJ/data/test/cardiomegaly")


a = ["G:/PROJEKT/INZPROJ/data/train/cardiomegaly/", "G:/PROJEKT/INZPROJ/data/valid/cardiomegaly/",
     "G:/PROJEKT/INZPROJ/data/train/nofindings/", "G:/PROJEKT/INZPROJ/data/valid/nofindings/",
     "G:/PROJEKT/INZPROJ/data/test/nofindings/", "G:/PROJEKT/INZPROJ/data/test/cardiomegaly/"]

for i in range(0, 6):
    path = a[i]
    dirs = os.listdir(path)
    for item in dirs:

        if os.path.isfile(path + item):
            im = Image.open(path + item)
            f, e = os.path.splitext(path + item)
            imResize = im.resize((224, 224), Image.ANTIALIAS)
            imResize.save(path + item)
