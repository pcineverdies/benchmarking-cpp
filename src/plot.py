import matplotlib.pyplot as plt
import numpy as np
import math
import sys

data   = []
counter = 0

def main():
    if(len(sys.argv)<2):
        return
        
    with open(sys.argv[1]+'.txt', 'r') as file:
        for x in file:
            data.append(int(x))
            counter = counter + 1

    data.sort()
    data = data[0:len(data)-math.floor(len(data)/100)]
    dataMax = max(data)
    dataMin = min(data)

    dim = dataMax - dataMin
    distance = 50
    elements = math.ceil(dim / distance)

    plot  = []
    xAxis = []

    for i in range(elements):
        plot.append(0)
        xAxis.append((i*distance)+dataMin)


    for elem in data:
        index = math.floor((elem-dataMin)/distance)
        plot[index] = plot[index] + 1


    (markers, stemlines, baseline) = plt.stem(xAxis,plot)
    plt.setp(markers, color="lightpink")
    plt.setp(stemlines, linestyle="-", color="limegreen", linewidth=0.5 )
    plt.setp(baseline, linestyle="-", color="black", linewidth=1)
    plt.xlabel('Time') 
    plt.ylabel('Number of occurrences') 
    plt.title(label=sys.argv[1])
    plt.show()

    plt.savefig(sys.argv[1])

if __name__ == "__main__":
    main()
