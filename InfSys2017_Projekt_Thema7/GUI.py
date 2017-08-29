#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter as tk


class Application(tk.Frame):
    def __init__(self, classifier, master=None, ):
        tk.Frame.__init__(self, master)
        self.classifier = classifier
        self.grid()
        self.initWidgets()

    def initWidgets(self):
        self.initInput()
        self.initButton()
        self.initResult()

    def initInput(self):
        self.labels = []
        self.entrys = []
        for element in range(1, len(self.classifier.identifier)):
            self.labels.append(tk.Label(self, text=self.classifier.identifier[element] + ":"))
            self.entrys.append(tk.Entry(self))
            self.labels[element - 1].grid()
            self.entrys[element - 1].grid()

    def initButton(self):
        self.button = tk.Button(self, text="Starte Klassifikation", command=self.onButtonPressed)
        self.button.grid()

    def onButtonPressed(self):
        featureList = []
        for element in range(0, len(self.entrys)):
            featureList.append(self.entrys[element].get())
        featureTuple = tuple(featureList)
        self.result["text"] = self.classifier.classifyTuple(featureTuple)

    def initResult(self):
        self.resultLabel = tk.Label(self, text="Klassifikations-Resultat:")
        self.result = tk.Label(self, text="-")
        self.result.grid()

def start(identifier):
        app = Application(identifier)
        app.master.title('Classifier GUI')
        app.mainloop()


