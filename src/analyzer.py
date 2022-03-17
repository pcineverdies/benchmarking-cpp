from statistics import mean, stdev, median
import sys

def main():
    data = []
    if(len(sys.argv)<2):
        return 

    name  = sys.argv[1]

    f = open(name + ".txt", "r")
    data = []
    for x in f:
        data.append(int(x))
    f.close()

    meanV = mean(data)
    stdevV = stdev(data)
    medianV = median(data)

    print("Mean", name, " : ", meanV, "us")
    print("Stdev", name, " : ", stdevV, "us")
    print("Median", name, " : ", medianV, "us")

if __name__ == "__main__":
    main()
