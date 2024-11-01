import os
from faker import Faker
import numpy.random as ran
import csv
import math

def genIncome():
    i = ran.choice([1,2,3,4],p=[0.4,0.5,0.09,.01])
    
    match i:
        case 1: return ran.randint(10000,50000)
        case 2: return ran.randint(20000,70000)
        case 3: return ran.randint(30000,100000)
        case 4: return ran.randint(40000,150000)

    
fake = Faker()
#def genFriendList(filesize):
    #return [ran.randrange(1,filesize) for j in range(ran.randrange(2,20))]
def _csvWriter(generator,filePath,):
    try:
        with open(filePath, "w", newline="") as fd:
            writer = csv.writer(fd,quoting=csv.QUOTE_STRINGS)
            lines = []
            i = 0
            for L in generator:
                i += 1
                lines.append(L)
            if len(lines) != 0:
                writer.writerows(lines)
    except Exception as e:
        print(f"Failed to write file {filePath}")
        print(f"Lines written {i}")
        print(e)
        

def genLargeFile(filePath, fileSize):
    _csvWriter(simulateLargeFile_G(fileSize),filePath)
    
def simulateLargeFile_G(fileSize):
    yield ["pid","name","address","income"]
    if fileSize == -1:
        i = 1
        while True:
            yield [i,fake.name(),fake.address().replace("\n",", "),genIncome()]
            i += 1
    else:
        for i in range(1,fileSize):
                yield [i,fake.name(),fake.address().replace("\n",", "),genIncome()]

def simulateSkewedData_G():
    lo,mid,hi = 1,10,100
    halfsize = 2000
    yield ["pid","name","address","income"]
    yield [1,fake.name(),fake.address().replace("\n",", "),mid]
    for i in range(halfsize):
        yield [i+1,fake.name(),fake.address().replace("\n",", "),lo]
    for i in range(halfsize):
        yield [i+1+halfsize,fake.name(),fake.address().replace("\n",", "),hi]

#100000000
def ReadFile(filepath: str):
    with open(filepath, "r") as fd:
        reader = csv.reader(fd)
        i = 0
        for row in reader:
            i+=1
            yield row
_prev = 0
def progressPrint(current:int,total:int,step=10):
    global _prev
    num = int(100*(current/total))
    if num != _prev and num%step == 0:
        print(f"{num}%")
    _prev = num
        
def generateTestFiles():
    os.makedirs("data",exist_ok=True)
    _csvWriter(simulateSkewedData_G(),"data/skewed.csv")
    print("data/skewed.csv: DONE")
    _csvWriter(simulateSkewedData_G(),"data/skewed.csv")