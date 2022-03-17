import matplotlib.pyplot as plt
import math

def plot(fileName, folder):
    data   = []
    counter = 0
        
    with open(folder + "/results/data.txt", 'r') as file:
        for x in file:
            data.append(int(x))
            counter = counter + 1

    data.sort()
    # Modificare data cleaning
    data = data[0:len(data)-math.floor(len(data)/100)]
    dataMax = max(data)
    dataMin = min(data)

    dim = dataMax - dataMin
    distance = dim / 100
    elements = math.ceil(dim / distance)

    plot  = []
    xAxis = []

    for i in range(elements):
        plot.append(0)
        xAxis.append((i*distance)+dataMin)


    for elem in data:
        index = math.floor((elem-dataMin)/distance)
        if index == elements:
            index = index - 1
        plot[index] = plot[index] + 1


    #Aggiungere opzioni visualizzazione
    (markers, stemlines, baseline) = plt.stem(xAxis,plot)
    plt.setp(markers, color="lightpink")
    plt.setp(stemlines, linestyle="-", color="limegreen", linewidth=0.5 )
    plt.setp(baseline, linestyle="-", color="black", linewidth=1)
    plt.xlabel('Time') 
    plt.ylabel('Number of occurrences') 
    #modificare titolo
    #plt.title()

    #salvare
    plt.savefig(folder+"/results/chart.eps", format="eps")
    plt.savefig(folder+"/results/chart.png")
