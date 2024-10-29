import re
import sys
import csv

def getCSV(filepath):
    reader = csv.reader()
    print(filepath)
    

def getLines(filepath):
    with open(filepath, "r",encoding="utf-8") as fd:
        line = fd.readline()
        header = line
        print(header)
        line = None
        while line is not None:
            line = fd.readline()
            yield line

                
def printInfo(line):
    print("--------------------------------------------------------------")#separator
    print(f"comma count: ({len(re.findall(",",line))})")
    print("--------------------------------------------------------------")#separator