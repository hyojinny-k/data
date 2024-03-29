import sys
from os import listdir
import numpy as np
import operator


def createDataSet(dirname):
    labels = []
    trainingFileList = listdir(dirname)
    m = len(trainingFileList)
    matrix = np.zeros((m, 1024))

    for i in range(m):
        fileNameStr = trainingFileList[i]
        answer = int(fileNameStr.split('_')[0])
        labels.append(answer)
        matrix[i, :] = getVector(dirname + '/' + fileNameStr)
    return matrix, labels


def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2  # 제곱
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5  # 루트
    sortedDistIndicies = distances.argsort()
    classCount = {}

    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True) # 내림차순
    return sortedClassCount[0][0] # max


def getVector(filename):
    vector = np.zeros((1, 1024))
    with open(filename) as f:
        for i in range(32):
            line = f.readline()
            for j in range(32):
                vector[0, 32 * i + j] = int(line[j])
        return vector


# trainingDir = sys.argv[1]
# testDir = sys.argv[2]
trainingDir = "trainingDigits"
testDir = "testDigits"
testFileList = listdir(testDir)
length = len(testFileList)
matrix, labels = createDataSet(trainingDir)

for k in range(1, 21): # 1~20
    count = 0 # 전체 파일 개수
    error = 0 # 예측을 실패한 경우

    for i in range(length):
        answer = int(testFileList[i].split('_')[0])
        testData = getVector(testDir + '/' + testFileList[i])
        classifiedResult = classify0(testData, matrix, labels, k)
        count += 1
        if answer != classifiedResult:
            error += 1
    print(int(error / count * 100)) # 에러율 -> int
