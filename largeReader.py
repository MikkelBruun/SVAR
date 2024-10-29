import csv
def ReadFile(filepath):
    with open(filepath, "r") as fd:
        reader = csv.reader(fd)
        for row in reader:
            yield row