import largeReader as lr
import heapq
import runningMedian

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
print(DH.Left)
print(DH.Right)
print(DH.median())
print(testLst[int(len(testLst)/2)])