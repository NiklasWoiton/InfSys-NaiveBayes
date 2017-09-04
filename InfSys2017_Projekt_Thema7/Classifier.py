#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import nltk
import random
import GUI


class NBClassifier(object):
    def __init__(self, csvDataSet):
        self.transformedData(csvDataSet)
        self.trainClassifier()
        GUI.start(self)

    """
    Creates a List of Tuples out of the CSV-DataSet and extracts the first Element,
    as it contains the Descriptions for the Columns and is not a Data-Point
    """
    def transformedData(self, csvDataSet):
        readCSV = csv.reader(open(csvDataSet, "rb"))
        self.listDataSet = [tuple(line) for line in readCSV]
        self.identifier = self.listDataSet.pop(0)
        random.shuffle(self.listDataSet)

    """
    Creates a List of 2-Part Tuples, containing all Features of a Row and the corresponding Class
    Out of this List it creates another List, also with 2-Part Tuples, 
    just this time with the Features transformed into a Dictionary
    Then it creates a Classifier with the help of the NLTK-Library,
    and either returns the accuracy of it or sets it as instance variable
    """
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

    #Transforms a Tuple of Features into a Dictionary of Features
    def featureTransformation(self, featureTuple):
        features = {}
        for element in range(1, len(featureTuple)):
            features[self.identifier[element]] = featureTuple[element]
        return features

    #Predicts a class for a given Tuple of Features
    def classifyTuple(self, featureTuple):
        return self.classifier.classify(self.featureTransformation(featureTuple))

    pass


nbClassifier = NBClassifier("workData.csv")
