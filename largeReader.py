import csv
def ReadFile(filepath: str):
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