from LineReader import getLines, printInfo


for i,data in enumerate(getLines("wsb_comments_raw.csv")):
    if(i > 100): break
    print(data)