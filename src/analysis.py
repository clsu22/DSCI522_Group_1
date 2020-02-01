# author: Margaret Zhao
# date: 2020-01-23

'''This script fits a model and outputs several images and csv reports

Usage: src/analysis.py --input=<input> --output=<output>

Options:
--input=<input>  Name of csv file to download, must be within the /data directory.
--output=<output>  Name of directory to be saved in, no slashes nesscesary, 'results' folder recommended. 
'''

#import packages
import pandas as pd
import altair as alt 
import matplotlib as plt
import numpy as np
from sklearn.model_selection import train_test_split

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

from sklearn.metrics import make_scorer, precision_score, f1_score, accuracy_score
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import recall_score, precision_score
from sklearn.metrics import roc_auc_score, roc_curve

import matplotlib.pyplot as plt
from docopt import docopt

opt = docopt(__doc__)

def main(input, output):
    # download cleaned data set xls to pandas dataframe
    df = pd.read_csv(f"./data/{input}")
    
    # Test to check the dimension of the data set
    assert df.shape == (
        275,10), "Wrong data set is loaded, check input file"
    
    
    # split training and test data set
    X = df.drop(columns=['Class'])
    y = df[['Class']]
    X_train, X_test, y_train, y_test = train_test_split(X,
                                                        y,
                                                        test_size=0.2,
                                                        random_state=888)
    
    # separate the features into numerical and categrocial columns.
    categorical_features = ['age', 'menopause', 'node_caps', 
                            'deg_malig', 'breast', 'breast_quad', 'irradiat']
    numeric_features = ['avg_tumor_size', 'avg_inv_nodes']

    # Scale the features according the type of features/create transformer 
    preprocessor = ColumnTransformer(
        transformers=[
            ('scale', StandardScaler(), numeric_features),
            ('ohe', OneHotEncoder(), categorical_features)])

    # Apply transformations and convert X_train and X_test into dataframe. 
    X_train = pd.DataFrame(preprocessor.fit_transform(X_train),
                          index=X_train.index,
                          columns=(numeric_features +
                                    list(preprocessor.named_transformers_['ohe']
                                        .get_feature_names(categorical_features))))
    X_test = pd.DataFrame(preprocessor.transform(X_test),
                          index=X_test.index,
                          columns=X_train.columns)
                          
    # Perform grid-search and cross-validation to find the best hyperparameter. 
    param_grid = {'C': [0.00001, 0.0001, 0.001, 0.01, 0.1, 1, 10, 100]}
    lgr = LogisticRegression(solver = 'liblinear')
    model = GridSearchCV(lgr, param_grid, cv=5, scoring='recall')
    model.fit(X_train, y_train.to_numpy().ravel());

    # Training with the best hyperparameter 
    best = LogisticRegression(solver = 'liblinear', C = 1)
    best.fit(X_train, y_train.to_numpy().ravel());
    weights = best.coef_
    
    # print out a table with the highest weighted feature at the top
    d = {'features' : list(X_train.columns),
         'weights': best.coef_.tolist()[0],
         'abs(weights)': abs(best.coef_).tolist()[0]}
    features_df = pd.DataFrame(d).sort_values(by = 'abs(weights)', ascending = False).reset_index(drop = True)
    features_df.to_csv(f'./{output}/features_and_weights.csv', index=False)

    # Plot a roc curve 
    plt.rc('font', size=18)          
    plt.rc('axes', titlesize=16, labelsize=16)    
    plt.rc('xtick', labelsize=16)    
    plt.rc('ytick', labelsize=16)    
    plt.rc('figure', titlesize=18)

    fpr, tpr, thresholds = roc_curve(y_test, model.predict_proba(X_test)[:,1])
    plt.plot(fpr, tpr);
    plt.title('ROC report')
    plt.plot((0,1),(0,1),'--k');
    plt.xlabel('False positive rate');
    plt.ylabel('True positive rate');
    plt.tight_layout()
    plt.savefig(f'./{output}/roc_report.png')
    
    # Tune threshold of Logistic regression to pick best threshold
    # Save scores csv file and plot a line plots
    from change_threshold import tune_threshold, test_threshold

    threshold_result = tune_threshold(best, X_train, y_train)
    threshold_result.to_csv(f'./{output}/model_threshold_tuning.csv', index=False)

    threshold_result.plot("threshold")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    plt.ylabel("score")
    plt.axvline(x=[0.22], color="r", linewidth=1, linestyle="--")
    plt.text(0.205, 0.73,'threshold=0.22', fontsize=11, color="r", rotation=90)
    plt.title("Scores in Logistic Regression with different threshold")
    plt.savefig(f'./{output}/threshold_scores.png', bbox_inches='tight')

    # Print out best C and threshold 
    pd.DataFrame({'hyperparameter': ['C', 'threshold'],
                   'value': [model.best_params_['C'], 0.22],
                   }).to_csv(f'./{output}/model_info.csv', index=False)

    # Apply model with tuned threshold to test dataset and print out scores 
    train_score = test_threshold(best, 0.22, X_train, y_train)
    test_score = test_threshold(best, 0.22, X_test, y_test)
    scores_df = pd.concat([train_score, test_score], axis=0)
    scores_df["dataset"] = ["train", "test"]
    scores_df = scores_df[["dataset", "accuracy", "recall", "precision", "f1_score", "roc_auc_score"]]
    scores_df.to_csv(f'./{output}/scores.csv', index=False)
    
    # Test to check the dimension of scores_df
    assert scores_df.shape == (
        2,6), "scores_df does not have the right dimension"
    
    
if __name__ == "__main__":
    main(input=opt["--input"], output=opt["--output"])
    
    
    
    
    
    





