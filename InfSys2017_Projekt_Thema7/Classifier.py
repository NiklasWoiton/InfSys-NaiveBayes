#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import nltk
import random
import GUI


class NBClassifier(object):
    def __init__(self, csvDataSet):
        self.csvDataSet = csvDataSet
        self.transformedData()
        self.trainClassifier()
        GUI.start(self)

    def transformedData(self):
        readCSV = csv.reader(open(self.csvDataSet, "rb"))
        self.listDataSet = [tuple(line) for line in readCSV]
        self.identifier = self.listDataSet.pop(0)
        random.shuffle(self.listDataSet)

    def trainClassifier(self, testPartition=0):
        features_class_tuples = [(self.listDataSet[i], self.listDataSet[i][0]) for i in range(0, len(self.listDataSet))]
        featureSet = [(self.featureTransformation(n), rating) for (n, rating) in features_class_tuples]
        if testPartition != 0:
            trainSet, testSet = featureSet[int(len(features_class_tuples) * testPartition):], featureSet[:int(
                len(features_class_tuples) * testPartition)]
            trainigsClassifier = nltk.NaiveBayesClassifier.train(trainSet)
            return nltk.classify.accuracy(trainigsClassifier, testSet)
        else:
            self.classifier = nltk.NaiveBayesClassifier.train(featureSet)

    def featureTransformation(self, featureTuple):
        features = {}
        for element in range(1, len(featureTuple)):
            features[self.identifier[element]] = featureTuple[element]
        return features

    def classifyTuple(self, featureTuple):
        return self.classifier.classify(self.featureTransformation(featureTuple))

    pass


nbClassifier = NBClassifier("workData.csv")
