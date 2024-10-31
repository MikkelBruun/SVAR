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
def genLargeFile(filepath, filesize):
    
    with open(filepath, "w", newline="") as fd:
        writer = csv.writer(fd,quoting=csv.QUOTE_STRINGS)
        header = ["pid","name","address","income"]
        writer.writerow(header)
        lines = []
        for i in range(1,filesize):
            lines.append([i,fake.name(),fake.address().replace("\n",", "),genIncome()])
            if len(lines) > 10000:
                writer.writerows(lines)
                lines = []
                print(f"{i}/{filesize}")
        if len(lines) != 0:
            writer.writerows(lines)
        print("Done")
def simulateLargeFile(filesize):
    yield ["pid","name","address","income"]
    for i in range(1,filesize):
            yield [i,fake.name(),fake.address().replace("\n",", "),genIncome()]