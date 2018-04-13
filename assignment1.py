import numpy as np
import matplotlib.pyplot as plt

def histogramGraph(dataSet, starting, numAttribute):
    bins = raw_input("Number of bins: ")
    y_axis = np.zeros(int(bins)) 

    for colNum in range(dataSet.shape[1]):
        colArray = dataSet[starting:numAttribute, colNum]
        print colArray
        min_colArray = min(colArray)
        max_colArray = max(colArray)
        binRange = float((max_colArray - min_colArray)) / int(bins)

        r1 = min_colArray
        r2 = min_colArray + binRange
        X = []
        for i in range(int(bins)):
            c = colArray[colArray > r1]
            c = c[c <= r2]
            y_axis[i] = c.size
            string = str(r1) + "-" + str(r2)
            X.append(string)
            r1 = r2
            r2 = r2 + binRange

        inds = np.arange(int(bins))
        width = 0.35
        p1 = plt.bar(inds, y_axis, width)
        print X
        plt.xticks(inds, X)
        plt.show()

def boxplotGraph(dataSet):
    for colNum in range(dataSet.shape[1]):
        plt.boxplot(dataSet[colNum])
        plt.show()

userinput = raw_input("Which data set to use? (Press 1 for iris.data.txt and 2 for wine.data.txt) ")

if (userinput == "1"):
    # load data set
    irisData = np.loadtxt('iris.data.txt', delimiter=',', usecols=(0, 1, 2, 3))

    option = raw_input("Press 1 to show histogram, and 2 for boxplot: ")
    if (option == "1"):
        classOption = raw_input("Press 1 for Iris Setosa, 2 for Iris Versicolor, 3 for Iris Virginica: ")
        if (classOption == "1"):
            histogramGraph(irisData, 0, 50)
        elif (classOption == "2"):
            histogramGraph(irisData, 50, 100)
        elif (classOption == "3"):
            histogramGraph(irisData, 100, 150)
    elif (option == "2"):
        boxplotGraph(irisData)
elif (userinput == "2"):
    wineData = np.loadtxt('wine.data.txt', delimiter=',', usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13))
    option = raw_input("Press 1 to show histogram, and 2 for boxplot: ")
    if (option == "1"):
        classOption = raw_input("Press 1 for Class 1, 2 for Class 2, and 3 for Class 3: ")
        if (classOption == "1"):
            histogramGraph(wineData, 0, 59)
        elif (classOption == "2"):
            histogramGraph(wineData, 59, 130)
        elif (classOption == "3"):
            histogramGraph(wineData, 130, 178)
    elif (option == "2"):
        boxplotGraph(wineData)