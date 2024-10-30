from faker import Faker
import random as ran
import csv
FILENAME = "fakeData.csv"
FILESIZE = 100000 #lines
PIDRANGE = range(1,FILESIZE)
INCOMERANGE = ran.randrange(12000,70000,500)

fake = Faker()
def genFriendList():
    return [ran.randrange(1,FILESIZE) for j in range(ran.randrange(2,20))]
with open(FILENAME, "w", newline="") as fd:
    writer = csv.writer(fd,quoting=csv.QUOTE_STRINGS)
    header = ["pid","name","address","income"]
    writer.writerow(header)
    lines = []
    for i in range(1,FILESIZE):
        lines.append([i,fake.name(),fake.address().replace("\n",", "),ran.randrange(12000,70000,500)])
        if len(lines) > 10000:
            writer.writerows(lines)
            lines = []
            print(f"{i}/{FILESIZE}")
    if len(lines) != 0:
        writer.writerows(lines)
    print("Done")
