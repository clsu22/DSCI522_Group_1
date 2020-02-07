# author: Haoyu Su
# date: 2020-01-31

'''This script is going to tune threshold of the logistic regression model and calculate scores

Usage: automaticlly called by analysis.py 
'''

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

from sklearn.metrics import make_scorer, precision_score, f1_score, accuracy_score
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import recall_score, precision_score
from sklearn.metrics import roc_auc_score, roc_curve

import matplotlib.pyplot as plt
from docopt import docopt

def tune_threshold(model, X_train, y_train):
    """
    Tune threshold of logistic regression

    Parameters:
    -----------
    model: object 
        A logistic regression model
    X_train: np.ndarray
        An array containing all features from training dataset 
    y_train: np.ndarray
        An array containing all targets from training dataset 
    """
    X_train2, X_valid, y_train2, y_valid = train_test_split(X_train,
                                                    y_train,
                                                    test_size=0.2,
                                                    random_state=888)
    model.fit(X_train2, y_train2.to_numpy().ravel());
    threshold_result = {"threshold":[], "accuracy":[], "recall":[], "precision":[], "roc_auc_score":[], "f1_score":[]}
    for THRESHOLD in [x*0.01 for x in range(50)]:
        preds = np.where(model.predict_proba(X_valid)[:,1] > THRESHOLD, 1, 0)
        threshold_result["threshold"].append(round(THRESHOLD, 2))
        threshold_result["accuracy"].append(accuracy_score(y_valid, preds))
        threshold_result["recall"].append(recall_score(y_valid, preds))
        threshold_result["precision"].append(precision_score(y_valid, preds))
        threshold_result["roc_auc_score"].append(roc_auc_score(y_valid, preds))
        threshold_result["f1_score"].append(f1_score(y_valid, preds))
        
    threshold_result = pd.DataFrame(threshold_result)
    return threshold_result

def test_threshold(model, t, X, y):
    """
    Calculate the scores by giving a threshold of logistic regression

    Parameters
    ----------
    model: object
        A logistic regression model
    t: float 
        A threshold to be used to calculate scores
    X: np.ndarray
        An array containing features
    y: np.ndarray
        An array containing targets
    """
    score_result = {"threshold":[], "accuracy":[], "recall":[], "precision":[], "roc_auc_score":[], "f1_score":[]}
    THRESHOLD = t
    preds = np.where(model.predict_proba(X)[:,1] > THRESHOLD, 1, 0)
    score_result["threshold"].append(round(THRESHOLD, 2))
    score_result["accuracy"].append(round(accuracy_score(y, preds), 2))
    score_result["recall"].append(round(recall_score(y, preds), 2))
    score_result["precision"].append(round(precision_score(y, preds), 2))
    score_result["roc_auc_score"].append(round(roc_auc_score(y, preds), 2))
    score_result["f1_score"].append(round(f1_score(y, preds), 2))

    score_result = pd.DataFrame(score_result)

    return score_result


if __name__ == "__main__":
    main()
