from faker import Faker
import random as ran
import csv
FILENAME = "fakeData.csv"
FILESIZE = 200 #lines
PIDRANGE = range(1,FILESIZE)
INCOMERANGE = ran.randrange(12000,70000,500)

fake = Faker()
def genFriendList():
    return [ran.randrange(1,FILESIZE) for j in range(ran.randrange(2,20))]
with open(FILENAME, "w", newline="") as fd:
    writer = csv.writer(fd,quoting=csv.QUOTE_STRINGS)
    header = ["pid","name","address","income","relationships"]
    writer.writerow(header)
    writer.writerows([i,fake.name(),fake.address().replace("\n",", "),ran.randrange(12000,70000,500),genFriendList()] for i in range(1,FILESIZE))
