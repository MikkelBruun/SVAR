import re
from matplotlib import pyplot as plt
import genData as gd
import sys
import runningMedian
import math

import visualize as vis

PROFILEDESC="""\
Available profiles
0   Generate a set of test files
1   Simulate a file with the desired size and process it
2   Runs the DualHeap median function on a dataset designed to specifically mess with it
3   Runs the DualHeap median function on a (simulted) infinite dataset.
    The intention is for the user to interupt the process, and then finish gracefully
    
"""


def readArgs():
    for arg in sys.argv:
        m = re.match(r"profile=(?P<profile>.*)",arg)
        if m is not None:
            match m.groupdict()["profile"]:
                case "0":
                    gd.generateTestFiles()
                case "1":
                    userInput = None
                    while userInput is None:
                        num = input("Generating large file. How many lines?")
                        try: 
                            userInput = int(num)
                        except Exception as e:
                            print(e)
                            print("please input a valid number")
                    processSimulatedFile(userInput)
                    print("Done")
                case "2":
                    print("""\
Processing a dataset with the following items:
    2000 rows:    income=1
    1 row:        income=10
    2000 rows:    income=100

The median shuold then be 10. However the DualHeap reports:""")
                    processSimulatedFile(gd.simulateSkewedData_G(),medianControl=True)
                case "3":
                    print("Simulating infinitely long dataset... press 'ctrl+c to interupt'")
                    processSimulatedFile(gd.simulateLargeFile_G(-1))
                case _:
                    print("unknown profile")

def processFile():
    DH = runningMedian.DualHeap()
    i = 0
    testLst = []
    for x in gd.ReadFile("fakeData.csv"):
        if i == 0: print(x)#header
        else:
            income = int(x[3])
            #print(income)
            DH.insert(income)
            testLst.append(income)
            
        i+=1
    testLst.sort()
    print(DH)
    print(testLst[int(len(testLst)/2)])

#meandianControl - naively test the median by sorting
def processSimulatedFile(dataGenerator,medianControl=False,printHeader=False):
    try:
        DH = runningMedian.DualHeap()
        i = 0
        #B = vis.getBuckets(range(10000,150000,5000))
        if medianControl: md = []
        for x in dataGenerator:
            if i == 0 and printHeader: print(x)#header
            else:
                income = int(x[3])
                #vis.bucketsInsert(B,income)
                DH.insert(income)
                if medianControl: md.append(income)
            i+=1
    except: 
        print(f"Interrupted after {i} items... current median:")
    finally:
        print(f"DualHeap median {DH.median()}")
        if medianControl:
            md = sorted(md)
            l = len(md)
            if l % 2 == 0:
                print(f"precise median ({md[(l/2)-1]},{md[l/2]})")
            else: print(f"precise median {md[math.floor(l/2)]}")

        
    #vis.barPlot(B,median = DH.median())
        
def main():
    readArgs()
    
main()

