import numpy as np
import utils
from sklearn.externals import joblib

def predictMLPClassifier(input):
    classifModel = joblib.load('classifModel')
    l = list()
    l.append(input)
    pred = classifModel.predict(l)
    return pred[0]