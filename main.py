from matplotlib import pyplot as plt
from genData import simulateLargeFile
import largeReader as lr

import runningMedian

import visualize as vis

def processFile():
    DH = runningMedian.DualHeap()
    i = 0
    testLst = []
    for x in lr.ReadFile("fakeData.csv"):
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
    
def processSimulatedFile():
    fileSize = 5000
    DH = runningMedian.DualHeap()
    i = 0
    B = vis.getBuckets(range(10000,150000,5000))
    for x in simulateLargeFile(fileSize):
        if i == 0: print(x)#header
        else:
            lr.progressPrint(i,fileSize)
            income = int(x[3])
            vis.bucketsInsert(B,income)
            #print(income)
            DH.insert(income)
        i+=1
    print(DH)
        
    vis.barPlot(B,median = DH.median())
        
processSimulatedFile()

