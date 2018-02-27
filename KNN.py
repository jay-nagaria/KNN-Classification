
import csv
import math
import operator

'''...............This program is personalized according to the IRIS dataset............... '''
'''..................if u wish to change the dataset please make the changes acordingly.................'''

'''--------------------------------------Break data set into training and testinig---------------------------------------------------------------------'''
trainingSet=[]
testSet=[]



with open('(dataset path)', 'r') as csvfile:
    lines = csv.reader(csvfile)
    dataset = list(lines)
    for x in range(len(dataset)-1):
        for y in range(4):
            dataset[x][y] = float(dataset[x][y])
        if x < 3*(len(dataset)/4):
            trainingSet.append(dataset[x])
        else:
            testSet.append(dataset[x])
                
print ('Training set: ' + repr(len(trainingSet)))
print ('Testing set: ' + repr(len(testSet)))

'''------------------------------------------Distance Calc-------------------------------------------------------'''   
                
def Distance(t1,t2,length):
    distance = 0
    for x in range(length):
        distance += math.pow(float(t1[x])-float(t2[x]),2)
    return math.sqrt(distance)
        
'''-------------------------------------fnd K neighbour------------------------------------------------------------'''        
def myknnclassify(X, test, k):
    distance = []
    length = len(test)-1   
    for x in range(len(X)):
        dist = Distance(X[x],test,length)
        distance.append((X[x],dist))
    distance.sort(key=operator.itemgetter(1))
    neighbour = []
    for x in range(k):
        neighbour.append(distance[x][0])  # value of neighbour
        
    for x in range(len(neighbour)):
        predict_class = {}
        if neighbour[x][-1] in predict_class:
            predict_class[neighbour[x][-1]] += 1
        else:
            predict_class[neighbour[x][-1]] = 1
            
    predict_class = sorted(predict_class.items(), key=operator.itemgetter(1), reverse=True)
    return predict_class[0][0]

'''----------------------------------Calc accuracy--------------------------------------------'''
def faccuracy(testSet, prediction):
    All = true_prediction = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == prediction[x]:
            true_prediction += 1
        All += 1
    return (true_prediction/All)*100




predictions=[]
k = 1
for x in range(len(testSet)):
	result = myknnclassify(trainingSet, testSet[x], k)
	predictions.append(result)
    
accuracy = faccuracy(testSet, predictions)
print('Accuracy: ' + repr(accuracy) + '%')
	
