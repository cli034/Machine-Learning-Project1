import numpy as np
import matplotlib.pyplot as plt


# make histogram graph
def histogramGraph(dataSet, starting, numAttribute):
    bins = raw_input("Number of bins: ")
    y_axis = np.zeros(int(bins)) 

    for colNum in range(dataSet.shape[1]):
        colArray = dataSet[starting:numAttribute, colNum]
        #print colArray
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

# make boxplot
def boxplotGraph(dataSet, starting, numAttribute):
    for colNum in range(dataSet.shape[1]):
        plt.boxplot(dataSet[starting:numAttribute, colNum])
        plt.show()

# calculate the correlation between two features
def correlation(dataSet, x, y):
    attr1 = dataSet[0:dataSet.shape[0], x]
    attr2 = dataSet[0:dataSet.shape[0], y]

    attr1Sum = 0
    attr1Mean = 0
    for i in attr1:
        attr1Sum = attr1Sum + i
    attr1Mean = attr1Sum / dataSet.shape[0]
    
    attr2Sum = 0
    attr2Mean = 0
    for j in attr2:
        attr2Sum = attr2Sum + j
    attr2Mean = attr2Sum / dataSet.shape[0]
    
    valueX = 0
    valueY = 0
    sumSqrX = 0
    sumSqrY = 0
    resultTmp = 0
    total = 0
    for i in range(dataSet.shape[0]):
        valueX = attr1[i] - attr1Mean
        valueY = attr2[i] - attr2Mean
        resultTmp = valueX * valueY
        total = total + resultTmp

        #for the standard deviation
        sumSqrX = sumSqrX + (valueX ** 2)
        sumSqrY = sumSqrY + (valueY ** 2)
        
    cov = total / dataSet.shape[0]

    sd_x = (sumSqrX / dataSet.shape[0]) ** (0.5)
    sd_y = (sumSqrY / dataSet.shape[0]) ** (0.5)

    corrl = cov / (sd_x * sd_y)
    return corrl

# make a 2D array based on the correlation between features
def makeCorrelationMatrix(dataSet):
    corrlMatrix = []
    
    for i in range(dataSet.shape[1]):
        temp = []
        for j in range(dataSet.shape[1]):
            if (i == j):
                temp.append(1)
            else:
                temp.append(correlation(dataSet,i,j))
        corrlMatrix.append(temp)
    return corrlMatrix

def heatmap(dataSet):
    arrayName = []
    if (dataSet.shape[1] == 4):
        arrayName.append("Sepal Length")
        arrayName.append("Sepal Width")
        arrayName.append("Petal Length")
        arrayName.append("Petal Width")
    elif (dataSet.shape[1] == 13):
        arrayName.append("Alcohol")
        arrayName.append("Malic Acid")
        arrayName.append("Ash")
        arrayName.append("Alcalinity of ash")
        arrayName.append("Magnesium")
        arrayName.append("Total phenols")
        arrayName.append("Flavanoids")
        arrayName.append("Nonflavanoid phenols")
        arrayName.append("Proanthocyanins")
        arrayName.append("Color intensity")
        arrayName.append("Hue")
        arrayName.append("OD280/OD315 of diluted wines")
        arrayName.append("Proline")
        
    temp = makeCorrelationMatrix(dataSet)

    a = np.array(temp)
    plt.imshow(a, cmap='hot', interpolation='nearest')
    plt.xticks(np.arange(dataSet.shape[1]), arrayName, rotation=90)
    plt.yticks(np.arange(dataSet.shape[1]), arrayName)
    plt.colorbar()
    plt.show()
    
    

userinput = raw_input("Which data set to use? (Press 1 for iris.data.txt and 2 for wine.data.txt) ")

if (userinput == "1"):
    # load data set
    irisData = np.loadtxt('iris.data.txt', delimiter=',', usecols=(0, 1, 2, 3))

    option = raw_input("Press 1 to show histogram, 2 for boxplot, 3 for correlation matrix ")
    if (option == "1"):
        classOption = raw_input("Press 1 for Iris Setosa, 2 for Iris Versicolor, 3 for Iris Virginica: ")
        if (classOption == "1"):
            histogramGraph(irisData, 0, 50)
        elif (classOption == "2"):
            histogramGraph(irisData, 50, 100)
        elif (classOption == "3"):
            histogramGraph(irisData, 100, 150)
    elif (option == "2"):
        classOption = raw_input("Press 1 for Iris Setosa, 2 for Iris Versicolor, 3 for Iris Virginica: ")
        if (classOption == "1"):
            boxplotGraph(irisData, 0, 50)
        elif (classOption == "2"):
            boxplotGraph(irisData, 50, 100)
        elif (classOption == "3"):
            boxplotGraph(irisData, 100, 150)
    elif (option == "3"):
        subOption = raw_input("Press 1 for just correlation matrix, 2 for heatmap ")
        if (subOption == "1"):
            print (makeCorrelationMatrix(irisData))
        elif (subOption == "2"):
            heatmap(irisData)
elif (userinput == "2"):
    wineData = np.loadtxt('wine.data.txt', delimiter=',', usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13))
    
    option = raw_input("Press 1 to show histogram, 2 for boxplot, 3 for correlation matrix ")
    if (option == "1"):
        classOption = raw_input("Press 1 for Class 1, 2 for Class 2, and 3 for Class 3: ")
        if (classOption == "1"):
            histogramGraph(wineData, 0, 59)
        elif (classOption == "2"):
            histogramGraph(wineData, 59, 130)
        elif (classOption == "3"):
            histogramGraph(wineData, 130, 178)
    elif (option == "2"):
        classOption = raw_input("Press 1 for Class 1, 2 for Class 2, and 3 for Class 3: ")
        if (classOption == "1"):
            boxplotGraph(wineData, 0, 59)
        elif (classOption == "2"):
            boxplotGraph(wineData, 59, 130)
        elif (classOption == "3"):
            boxplotGraph(wineData, 130, 178)
    elif (option == "3"):
        subOption = raw_input("Press 1 for just correlation matrix, 2 for heatmap ")
        if (subOption == "1"):
            print (makeCorrelationMatrix(wineData))
        elif (subOption == "2"):
            heatmap(wineData)