import numpy as np
import matplotlib.pyplot as plt


# make histogram graph
# histogram is graphed for each class
# Question 1.1
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
# boxplot is graphed for each class
# Question 1.2
def boxplotGraph(dataSet, starting, numAttribute):
    for colNum in range(dataSet.shape[1]):
        plt.boxplot(dataSet[starting:numAttribute, colNum])
        plt.show()

# calculate the correlation between two features
# Question 2.1.a
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
# Feature by feature correlation matrix
# Question 2.1.b
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

# make a heatmap of the Feature by feature correlation matrix
# Question 2.1.d
def heatmap(dataSet):
    temp = makeCorrelationMatrix(dataSet)
    if (dataSet.shape[1] == 4):
        a = np.array(temp)
        plt.imshow(a, cmap='hot', interpolation='nearest')
        plt.xticks(np.arange(dataSet.shape[1]), irisFeatureName)
        plt.yticks(np.arange(dataSet.shape[1]), irisFeatureName)
        plt.colorbar()
        plt.show()
    elif (dataSet.shape[1] == 13):
        a = np.array(temp)
        plt.imshow(a, cmap='hot', interpolation='nearest')
        plt.xticks(np.arange(dataSet.shape[1]), wineFeatureName, rotation=90)
        plt.yticks(np.arange(dataSet.shape[1]), wineFeatureName)
        plt.colorbar()
        plt.show()
        
# make scatter plot for feature pairs (only for iris data)
# Question 2.2.a
def scatterPlot(dataSet):
    for i in range(dataSet.shape[1]):
        for j in range(dataSet.shape[1]):
            # you don't plot with the same feature
            # you don't plot repeated pairs, thats why j is always greater than i
            if ((i != j) and (i < j)):
                #separate feature pairs by colors depand on its class
                x_class1 = dataSet[0:50,i]
                y_class1 = dataSet[0:50,j]
                color1 = ['red']

                x_class2 = dataSet[50:100,i]
                y_class2 = dataSet[50:100,j]
                color2 = ['green']

                x_class3 = dataSet[100:150,i]
                y_class3 = dataSet[100:150,j]
                color3 = ['blue']

                plt.scatter(x_class1, y_class1, c=color1, s=50)
                plt.scatter(x_class2, y_class2, c=color2, s=50)
                plt.scatter(x_class3, y_class3, c=color3, s=50)

                plt.title(irisFeatureName[i] + " VS " + irisFeatureName[j] + "\n Red - Setosa, Green - Versicolor, Blue - Virginica")
                plt.xlabel(irisFeatureName[i])
                plt.ylabel(irisFeatureName[j])
                plt.show()

# Lp norm distance formula
# Questio 2.3.a
def distance(x,y,p):
    array1 = x
    array2 = y
    temp = 0
    total = 0
    distance = 0

    for i in range(len(array1)):
        temp = abs(array1[i] - array2[i]) ** p
        total = total + temp
    
    distance = total ** (float(1)/p)
    return distance

#distance when p=1
#Question 2.3.b    
def distance_p1(dataSet):
    distance_p1 = []
    for i in range(dataSet.shape[0]):
        temp1 = []
        for j in range(dataSet.shape[0]):
            # do not repeat for pairs that has been comupted, if i==i means the same flower, the distance should be 0
            flower1 = dataSet[i]
            flower2 = dataSet[j]

            temp1.append(distance(flower1,flower2,1))
        distance_p1.append(temp1)
    #print distance_p1
    return distance_p1

#distance when p=2
#Queston 2.3.b
def distance_p2(dataSet):
    distance_p2 = []
    for i in range(dataSet.shape[0]):
        temp2 = []
        for j in range(dataSet.shape[0]):
            # do not repeat for pairs that has been comupted, if i==i means the same flower, the distance should be 0
            flower1 = dataSet[i]
            flower2 = dataSet[j]

            temp2.append(distance(flower1,flower2,2))
        distance_p2.append(temp2)
    #print distance_p2
    return distance_p2

#heatmap when p=1
#Question 2.3.d
def distance_p1_heatmap(dataSet):
    temp = distance_p1(dataSet)
    #flower_num = []
    #for i in range(dataSet.shape[0]):
        #flower_num.append(i)
    a = np.array(temp)
    plt.imshow(a, cmap='hot', interpolation='nearest')
    #plt.xticks(np.arange(dataSet.shape[0]), flower_num)
    #plt.yticks(np.arange(dataSet.shape[0]), flower_num)
    plt.title("Distance Heatmap for each flower, p = 1")
    plt.colorbar()
    plt.show()

#heatmap when p=2
#Question 2.3.d
def distance_p2_heatmap(dataSet):
    temp = distance_p2(dataSet)
    a = np.array(temp)
    plt.imshow(a, cmap='hot', interpolation='nearest')
    #plt.xticks(np.arange(dataSet.shape[1]), irisFeatureName)
    #plt.yticks(np.arange(dataSet.shape[1]), irisFeatureName)
    plt.title("Distance Heatmap for each flower, p = 2")
    plt.colorbar()
    plt.show()
    

userinput = raw_input("Which data set to use? (Press 1 for iris.data.txt and 2 for wine.data.txt) ")

if (userinput == "1"):
    # load data set
    irisData = np.loadtxt('iris.data.txt', delimiter=',', usecols=(0, 1, 2, 3))
    irisFeatureName = []
    irisFeatureName.append("Sepal Length")
    irisFeatureName.append("Sepal Width")
    irisFeatureName.append("Petal Length")
    irisFeatureName.append("Petal Width")
    
    #print(distance(irisData[0:irisData.shape[0], 0],irisData[0:irisData.shape[0], 1],2))
    #print irisData[0]
    option = raw_input("Press 1 to show histogram, 2 for boxplot, 3 for correlation matrix, 4 for scatter plot, 5 for distance matrix")
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
    elif (option == "4"):
        scatterPlot(irisData)
    elif (option == "5"):
        subOption = raw_input("Press 1 for p = 1, 2 for p = 2 ")
        if (subOption == "1"):
            sub_subOption = raw_input("Press 1 for matrix, 2 for heatmap ")
            if (sub_subOption == "1"):
                print(distance_p1(irisData))
            elif (sub_subOption == "2"):
                distance_p1_heatmap(irisData)
        elif (subOption == "2"):
            sub_subOption = raw_input("Press 1 for matrix, 2 for heatmap ")
            if (sub_subOption == "1"):
                print(distance_p2(irisData))
            elif (sub_subOption == "2"):
                distance_p2_heatmap(irisData)
elif (userinput == "2"):
    wineData = np.loadtxt('wine.data.txt', delimiter=',', usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13))
    wineFeatureName = []
    wineFeatureName.append("Alcohol")
    wineFeatureName.append("Malic Acid")
    wineFeatureName.append("Ash")
    wineFeatureName.append("Alcalinity of ash")
    wineFeatureName.append("Magnesium")
    wineFeatureName.append("Total phenols")
    wineFeatureName.append("Flavanoids")
    wineFeatureName.append("Nonflavanoid phenols")
    wineFeatureName.append("Proanthocyanins")
    wineFeatureName.append("Color intensity")
    wineFeatureName.append("Hue")
    wineFeatureName.append("OD280/OD315 of diluted wines")
    wineFeatureName.append("Proline")
    
    option = raw_input("Press 1 to show histogram, 2 for boxplot, 3 for correlation matrix, 4 for distance matrix ")
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
    elif (option == "4"):
        subOption = raw_input("Press 1 for p = 1, 2 for p = 2 ")
        if (subOption == "1"):
            sub_subOption = raw_input("Press 1 for matrix, 2 for heatmap ")
            if (sub_subOption == "1"):
                print(distance_p1(wineData))
            elif (sub_subOption == "2"):
                distance_p1_heatmap(wineData)
        elif (subOption == "2"):
            sub_subOption = raw_input("Press 1 for matrix, 2 for heatmap ")
            if (sub_subOption == "1"):
                print(distance_p2(wineData))
            elif (sub_subOption == "2"):
                distance_p2_heatmap(wineData)