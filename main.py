import re
from types import CodeType
from matplotlib import pyplot as plt
import genData as gd
import sys
import runningMedian
import math
import cProfile
import pstats

import visualize as vis

PROFILEDESC="""\
Available profiles (symbol meaning [v=the result is visualized,p=the execution is profiled])
0   Generate a set of test files
1   [v] Runs the DualHeap median function on the main dataset
2   Runs the DualHeap median function on a dataset designed to specifically mess with it
3   [v] Runs the DualHeap median function on a (simulted) infinite dataset.
    The intention is for the user to interupt the process, and then finish gracefully
4   [p] Runs the DualHeap median function on the main dataset
5   [p] Runs the DualHeap median function on a (simulted) infinite dataset.
"""
PROFILE = cProfile.Profile()

def readArgs():
    for arg in sys.argv:
        m = re.match(r"profile=(?P<profile>.*)",arg)
        if m is not None:
            match m.groupdict()["profile"]:
                case "0":
                    gd.generateTestFiles()
                case "1":
                    processData(gd.ReadFile_G("data/main.csv"),medianControl=True,visualize="data/main.csv")
                case "2":
                    print("""\
Processing a dataset with the following items:
    2000 rows:    income=1
    1 row:        income=10
    2000 rows:    income=100

The median shuold then be 10. However the DualHeap reports:""")
                    processData(gd.simulateSkewedData_G(),medianControl=True)
                case "3":
                    print("Simulating infinitely long dataset... press 'ctrl+c to interupt'")
                    
                    processData(gd.simulateLargeFile_G(-1),
                                medianControl=True,
                                visualize="'infinitely' large dataset")
                case "4":
                    print("Profiling on data/main.csv")
                    processData(gd.ReadFile_G("data/main.csv"),profile=True)
                case "5":
                    print("Profiling on infinitely long dataset... press 'ctrl+c to interupt'")
                    processData(gd.simulateLargeFile_G(-1),
                                medianControl=True,
                                profile=True)

                case _:
                    print("unknown profile")
                    print(PROFILEDESC)
    


#meandianControl - naively test the median by sorting
def processData(
    dataGenerator,
    medianControl=False,
    printHeader=False,
    visualize:str=None,
    profile=False
):
    
    visualizeTitle = visualize
    if(visualize is not None): visualize = True # kinda hacky but i awnted to add titles late in the day
    if(profile): PROFILE.enable()
    try:
        DH = runningMedian.DualHeap()
        i = 0
        if visualize: B = vis.getBuckets(range(10000,230000,5000))
        if medianControl: md = []
        for x in dataGenerator:
            if i == 0 :
                if printHeader: print(x)#header
            else:
                income = int(x[3])
                if visualize:vis.bucketsInsert(B,income)
                DH.insert(income)
                if medianControl: md.append(income)
            i+=1
    except KeyboardInterrupt: 
        print(f"Interrupted after {i} items... current median:")
    except Exception as e:
        print(i)
        print(e) 
    finally:
        print(f"DualHeap median {DH.median()}")
        if medianControl:
            md = sorted(md)
            l = len(md)
            if l % 2 == 0:
                print(f"precise median ({md[(math.floor(l/2))-1]},{md[math.floor(l/2)]})")
            else: print(f"precise median {md[math.floor(l/2)]}")
        if profile:
            PROFILE.create_stats()
            PROFILE.print_stats(sort="tottime")
        if(visualize):
            vis.barPlot(B,title=visualizeTitle,median=DH.median())
def main():
    readArgs()
    
main()

