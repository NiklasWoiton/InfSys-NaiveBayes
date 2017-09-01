#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter as tk
import math


class GUI(tk.Frame):
    def __init__(self, classifier, master=None, ):
        tk.Frame.__init__(self, master)
        self.classifier = classifier
        self.grid()
        self.featureLabels = []
        self.entries = []
        self.topLabel = None
        self.classifyButton = None
        self.classifierResultLabel = None
        self.classifierResult = None
        self.accuracyTestButton = None
        self.accuracyLabel = None
        self.initWidgets()

    def initWidgets(self):
        self.initClassifier()
        self.initAccuray()
        self.initLayout()

    def initClassifier(self):
        self.topLabel = (tk.Label(self, text="Bewertungen von 0 bis 5"))
        for element in range(1, len(self.classifier.identifier)):
            self.featureLabels.append(tk.Label(self, text=self.classifier.identifier[element] + ":"))
            self.entries.append(tk.Entry(self))
        self.classifyButton = tk.Button(self, text="Start", command=self.onClassifyButtonPressed)
        self.classifierResultLabel = tk.Label(self, text=self.classifier.identifier[0] + ":")
        self.classifierResult = tk.Label(self, text="-")

    def onClassifyButtonPressed(self):
        featureList = []
        for element in range(1, len(self.entries)):
            try:
                if self.entries[element].get() is "":
                    featureList.append(-1)
                elif -1 <= int(self.entries[element].get()) <= 5:
                    featureList.append(self.entries[element].get())
                else:
                    break
            except:
                break
        if len(featureList) == len(self.entries)-1:
            self.classifierResult["text"] = self.classifier.classifyTuple(tuple(featureList))
        else:
            self.classifierResult["text"] = "INVALID INPUT"

    def initAccuray(self):
        testPartition = 0.9
        self.accuracyLabel = tk.Label(self, text="(Klassifikationsgenauigkeit von ≈ " + str(int(math.floor(self.classifier.trainClassifier(testPartition) * 100))) + "%)")

    def initLayout(self):
        self.topLabel.grid(row=0, column=0, columnspan=2)
        for element in range(0, len(self.featureLabels)):
            self.featureLabels[element].grid(row=element+1, column=0)
            self.entries[element].grid(row=element+1, column=1)
        self.classifyButton.grid(row=len(self.featureLabels)+1, column=1)
        self.classifierResultLabel.grid(row=len(self.featureLabels) + 2, column=0)
        self.classifierResult.grid(row=len(self.featureLabels) + 2, column=1)
        self.accuracyLabel.grid(row=len(self.featureLabels) + 3, column=0, columnspan=2)


def start(identifier):
        gui = GUI(identifier)
        gui.master.title('Naive-Bayes-Klassifikator')
        gui.mainloop()


