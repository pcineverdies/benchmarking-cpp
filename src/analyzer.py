from statistics import mean, stdev, median
from termcolor import colored

def analyzeData(fileName):

    f = open(fileName , "r")
    data = []
    for x in f:
        data.append(int(x))
    f.close()

    meanV = mean(data)
    stdevV = stdev(data)
    medianV = median(data)

    print(colored("===========================================", "magenta"))
    print("Mean  : ", meanV, "us")
    print("Stdev  : ", stdevV, "us")
    print("Median : ", medianV, "us")
    print(colored("===========================================", "magenta"))

