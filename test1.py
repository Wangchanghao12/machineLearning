#encoding=gbk
from math import log
def creatDataSet():
    # ���ݼ�
    dataSet=[[0, 0, 0, 0, 'no'],
            [0, 0, 0, 1, 'no'],
            [0, 1, 0, 1, 'yes'],
            [0, 1, 1, 0, 'yes'],
            [0, 0, 0, 0, 'no'],
            [1, 0, 0, 0, 'no'],
            [1, 0, 0, 1, 'no'],
            [1, 1, 1, 1, 'yes'],
            [1, 0, 1, 2, 'yes'],
            [1, 0, 1, 2, 'yes'],
            [2, 0, 1, 2, 'yes'],
            [2, 0, 1, 1, 'yes'],
            [2, 1, 0, 1, 'yes'],
            [2, 1, 0, 2, 'yes'],
            [2, 0, 0, 0, 'no']]
    #��������
    labels=['����','�й���','���Լ��ķ���','�Ŵ����']
    #�������ݼ��ͷ�������
    return dataSet,labels



def calcShannonEnt(dataSet):
    #�������ݼ�����
    numEntries=len(dataSet)
    #����ÿ����ǩ��label�����ִ������ֵ�
    labelCounts={}
    #��ÿ��������������ͳ��
    for featVec in dataSet:
        currentLabel=featVec[-1]                     #��ȡ��ǩ��Ϣ
        if currentLabel not in labelCounts.keys():   #�����ǩû�з���ͳ�ƴ������ֵ䣬���ӽ�ȥ
            labelCounts[currentLabel]=0
        labelCounts[currentLabel]+=1                 #label����

    shannonEnt=0.0                                   #������
    #���㾭����
    for key in labelCounts:
        prob=float(labelCounts[key])/numEntries      #ѡ��ñ�ǩ�ĸ���
        shannonEnt-=prob*log(prob,2)                 #���ù�ʽ����
    return shannonEnt                                #���ؾ�����




def chooseBestFeatureToSplit(dataSet):
    #��������
    numFeatures = len(dataSet[0]) - 1
    #�������ݼ�����ũ��
    baseEntropy = calcShannonEnt(dataSet)
    #��Ϣ����
    bestInfoGain = 0.0
    #��������������ֵ
    bestFeature = -1
    #������������
    for i in range(numFeatures):
        # ��ȡdataSet�ĵ�i����������
        featList = [example[i] for example in dataSet]
        #����set����{}��Ԫ�ز����ظ�
        uniqueVals = set(featList)
        #����������
        newEntropy = 0.0
        #������Ϣ����
        for value in uniqueVals:
            #subDataSet���ֺ���Ӽ�
            subDataSet = splitDataSet(dataSet, i, value)
            #�����Ӽ��ĸ���
            prob = len(subDataSet) / float(len(dataSet))
            #���ݹ�ʽ���㾭��������
            newEntropy += prob * calcShannonEnt((subDataSet))
        #��Ϣ����
        infoGain = baseEntropy - newEntropy
        #��ӡÿ����������Ϣ����
        print("��%d������������Ϊ%.3f" % (i, infoGain))
        #������Ϣ����
        if (infoGain > bestInfoGain):
            #������Ϣ���棬�ҵ�������Ϣ����
            bestInfoGain = infoGain
            #��¼��Ϣ������������������ֵ
            bestFeature = i
            #������Ϣ�����������������ֵ
    return bestFeature


def splitDataSet(dataSet,axis,value):
    retDataSet=[]
    for featVec in dataSet:
        if featVec[axis]==value:
            reducedFeatVec=featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet


#main����
if __name__=='__main__':
    dataSet,features=creatDataSet()
    # print(dataSet)
    # print(calcShannonEnt(dataSet))
    print("��������ֵ��"+str(chooseBestFeatureToSplit(dataSet)))