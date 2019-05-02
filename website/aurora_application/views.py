from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render

from aurora_application.models import IMG

from sklearn.linear_model import RidgeClassifier
from sklearn.metrics import confusion_matrix

import h5py
import numpy as np
import pandas as pd
import numpy.random as rand
# import example_feat_extract

# efe = example_feat_extract


# from __future__ import absolute_import
# from __future__ import division
# from __future__ import print_function
#
# import argparse
# import numpy as np
# import time
# from datetime import datetime
# import os
# # import sys


# te/aurora_application/feature_extractor/feature_extractor.py"
# sys.path.append("/Users/xcliang/Documents/GitHub/project-21-aurora_borealis_classification/website/aurora_application/feature_extractor")
# extractor =
# import utils
# from feature_extractor.feature_extractor import FeatureExtractor




# Create your views here.
def index(request):
    # template = loader.get_template('templates/aurora_main.html')
    return render(request, 'aurora_main.html')

def home(request):
    return render(request, 'aurora_main.html')

def contact(request):
    return render(request, "contact.html")

def upload(request):
    # if request.method == 'POST':
    #     img = IMG(img_url=request.FILES.get('img'))
    #     img.save()
    return render(request, 'upload.html')

# def show(request):
#     new_img = IMG(img=request.FILES.get('img'))
#     new_img.save()
#     content = {
#         'aaa': new_img,
#     }
#     return render(request, 'show.html', content)

def show(request):
    new_img = IMG(img=request.FILES.get('img'))
    new_img.save()

    # efe.get_features()

    y_pred = train()
    
    category = get_category(y_pred)

    content = {
        'category': category,
    }
    return render(request, 'show.html', content)

def train():
    base_dir = "/Users/xcliang/Documents/Github/project-21-aurora_borealis_classification/oath_v1.1/"

    # read classifications
    df = pd.read_csv(base_dir + "classifications/classifications.csv", skiprows=18)
    ndata = len(df["picNum"])

    f = h5py.File(base_dir + "features/auroral_feat.h5", "r")
    features = f["Logits"].value
    f.close()

    alpha = 0.03
    avgscore = np.zeros(5)

    idxs = np.loadtxt(base_dir + "classifications/train_test_split.csv", delimiter=",").astype(int)
    cnt = 0
    for idx in idxs:
        ntrain = int(np.round(0.7 * ndata))
        idx_train = idx[0:ntrain]
        idx_test = idx[ntrain:]

        # use 'class2' here to train machine on two classes
        # only, aurora and non-aurora (instead of 'class6')
        X_train = features[idx_train, :]
        y_train = df["class6"][idx_train]
        X_test = features[idx_test, :]
        y_test = df["class6"][idx_test]

        clf = RidgeClassifier(random_state=10 * cnt, normalize=False, alpha=alpha)
        clf.fit(X_train, y_train)
        avgscore[cnt] = clf.score(X_test, y_test)
        cnt += 1

    y_pred = clf.predict(X_test[:10])
    return(y_pred[3])

    # data_dir = "/Users/xcliang/Documents/GitHub/project-21-aurora_borealis_classification/website/media/"
    # trained_classifier = clf
    #
    # f = h5py.File(data_dir + "features/auroral_feat.h5", "r")
    # features_test = f["Logits"].value
    # f.close()
    #
    # pred = trained_classifier.predict(features_test)
    # print(pred)

def get_category(y_pred):
    d = {1 : 'Arc',
        2 : 'Diffuse',
        3 : 'Discrete',
        4 : 'Cloudy',
        5 : 'Moon',
        6 : 'Clear /Noaurora'}
    category = d[y_pred]
    return(category)
