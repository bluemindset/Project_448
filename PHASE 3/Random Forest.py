# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 00:03:44 2019

@author: Stefanos Ioannou
"""
import pandas as pd
import numpy as np
import sklearn.metrics as m
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

test=pd.read_csv("test.csv")
train=pd.read_csv("train.csv")

xtrain=train.iloc[:,1:15]
ytrain=train['res']

xtest=test.iloc[:,1:15]
ytest=test['res']

#Increasing depth yelds better results
clf = RandomForestClassifier(n_estimators=100, max_depth=200, random_state=0)
clf = clf.fit(xtrain, ytrain)
ynew = clf.predict(xtest)
print(accuracy_score(ynew, ytest))