#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter as tk


class GUI(tk.Frame):
    def __init__(self, classifier, master=None, ):
        tk.Frame.__init__(self, master)
        self.classifier = classifier
        self.grid()
        self.featureLabels = []
        self.entries = []
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
        self.featureLabels.append(tk.Label(self, text="Features"))
        self.entries.append(tk.Label(self, text="Ratings from 0 to 5"))
        for element in range(1, len(self.classifier.identifier)):
            self.featureLabels.append(tk.Label(self, text=self.classifier.identifier[element] + ":"))
            self.entries.append(tk.Entry(self))
        self.classifyButton = tk.Button(self, text="Starte Klassifikation", command=self.onClassifyButtonPressed)
        self.classifierResultLabel = tk.Label(self, text="Klassifikation:")
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
        self.accuracyLabel = tk.Label(self, text="(Mit " + str(self.classifier.trainClassifier(testPartition) * 100) +  "% Genauigkeit)")

    def initLayout(self):
        for element in range(0, len(self.featureLabels)):
            self.featureLabels[element].grid(row=element, column=0)
            self.entries[element].grid(row=element, column=1)
        self.classifyButton.grid(row=len(self.featureLabels), column=1)
        self.classifierResultLabel.grid(row=len(self.featureLabels) + 1, column=0)
        self.classifierResult.grid(row=len(self.featureLabels) + 1, column=1)
        self.accuracyLabel.grid(row=len(self.featureLabels), column=3)


def start(identifier):
        gui = GUI(identifier)
        gui.master.title('Classifier GUI')
        gui.mainloop()


