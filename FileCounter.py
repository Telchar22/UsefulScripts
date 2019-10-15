import os
path = "path to dir"
allfiles = os.listdir(path)
number_files = len(allfiles)
print(number_files)

onlyfiles = next(os.walk(path))[2]
print(len(onlyfiles))

print(len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))]))
