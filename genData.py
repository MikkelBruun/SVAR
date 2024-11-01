import os
from faker import Faker
import numpy.random as ran
import csv
import math


income_gen_log = None #a global value, only generated once
choice_gen = ran.default_rng()
def genIncome(log=False):
    global income_gen_log
    global choice_gen
    if log:
        if income_gen_log is None: 
            income_gen_log = list(genIncomeProbabilities())
        v,p = income_gen_log
        return choice_gen.choice(v,p=p)+ran.randint(0,30000)
    else:
        i = choice_gen.choice([1,2,3,4],p=[0.4,0.5,0.09,.01])
        match i:
            case 1: return ran.randint(10000,50000)
            case 2: return ran.randint(20000,70000)
            case 3: return ran.randint(30000,100000)
            case 4: return ran.randint(40000,150000)

def genIncomeProbabilities():
    lo,hi, step = 10000, 200000, 10000
    values = [v for v in range(lo,hi,step)]
    logs = [math.log(v) for v in values]
    dLogs = []
    for i in range(len(logs)):
        if(i+1<len(logs)):
            dLogs.append(logs[i+1]-logs[i])
        else: dLogs.append(dLogs[i-1])
    total = sum(dLogs)
    return (values,list(map(lambda x: x/total,dLogs)))

fake = Faker()

def _csvWriter(generator,filePath,):
    try:
        with open(filePath, "w", newline="") as fd:
            writer = csv.writer(fd,quoting=csv.QUOTE_STRINGS)
            lines = []
            i = 0
            try:
                for L in generator:
                    i += 1
                    lines.append(L)
                    if(len(lines)>1000):
                        writer.writerows(lines)
                        lines = []
                if len(lines) != 0:
                    writer.writerows(lines)
            except KeyboardInterrupt:
                print("Interupted by user")
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
    if fileSize == -1:#infinitefile
        i = 1
        while True:
            yield [i,fake.name(),fake.address().replace("\n",", ")
                   ,genIncome(log=False)] #using log is much slower
            i += 1
    else:
        for i in range(1,fileSize):
                yield [i,fake.name(),fake.address().replace("\n",", "),genIncome(log=True)]

def simulateSkewedData_G():
    lo,mid,hi = 1,10,100
    halfsize = 2000
    yield ["pid","name","address","income"]
    yield [1,fake.name(),fake.address().replace("\n",", "),mid]
    for i in range(halfsize):
        yield [i+1,fake.name(),fake.address().replace("\n",", "),lo]
    for i in range(halfsize):
        yield [i+1+halfsize,fake.name(),fake.address().replace("\n",", "),hi]


def ReadFile_G(filepath: str):
    with open(filepath, "r") as fd:
        reader = csv.reader(fd)
        for row in reader:
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
    print("data/skewed.csv: ",sep="")
    _csvWriter(simulateSkewedData_G(),"data/skewed.csv")
    print("DONE")
    print("data/main.csv: ",sep="")
    print("INFO: This may take some time. Press ctrl+c to stop the generation. Progress is saved")
    _csvWriter(simulateLargeFile_G(1000000),"data/main.csv")
    print("DONE")
    