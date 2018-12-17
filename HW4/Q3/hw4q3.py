## Data and Visual Analytics - Homework 4
## Georgia Institute of Technology
## Applying ML algorithms to detect seizure

import numpy as np
import pandas as pd
import time

from sklearn.model_selection import cross_val_score, GridSearchCV, cross_validate, train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.svm import SVC
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, normalize

######################################### Reading and Splitting the Data ###############################################
# XXX
# TODO: Read in all the data. Replace the 'xxx' with the path to the data set.
# XXX
data = pd.read_csv('seizure_dataset.csv')

# Separate out the x_data and y_data.
x_data = data.loc[:, data.columns != "y"]
y_data = data.loc[:, "y"]

# The random state to use while splitting the data.
random_state = 100

# XXX
# TODO: Split 70% of the data into training and 30% into test sets. Call them x_train, x_test, y_train and y_test.
# Use the train_test_split method in sklearn with the paramater 'shuffle' set to true and the 'random_state' set to 100.
# XXX

X_train, X_test, y_train, y_test = train_test_split(x_data, y_data, shuffle=True, test_size=0.3,random_state=random_state)

# ############################################### Linear Regression ###################################################
# XXX
# TODO: Create a LinearRegression classifier and train it.
# XXX
LR = LinearRegression()
LR.fit(X_train, y_train)

LR_trian_predict = LR.predict(X_train).round()
LR_train_ACC = accuracy_score(y_train, LR_trian_predict)

LR_test_predict = LR.predict(X_test).round()
LR_test_ACC = accuracy_score(y_test, LR_test_predict)

print("LR Accuracy Training %.3f" %(LR_train_ACC))
print("LR Accuracy Testing %.3f" %(LR_test_ACC))
# XXX
# TODO: Test its accuracy (on the training set) using the accuracy_score method.
# TODO: Test its accuracy (on the testing set) using the accuracy_score method.
# Note: Use y_predict.round() to get 1 or 0 as the output.
# XXX


# ############################################### Multi Layer Perceptron #################################################
# XXX
# TODO: Create an MLPClassifier and train it.
# XXX
MLP = MLPClassifier(random_state=random_state)
MLP.fit(X_train, y_train)

MLP_train_predict = MLP.predict(X_train)
MLP_train_ACC = accuracy_score(y_train, MLP_train_predict)

MLP_test_predict = MLP.predict(X_test)
MLP_test_ACC = accuracy_score(y_test, MLP_test_predict)

print("MLP Accuracy Training %.3f" %(MLP_train_ACC))
print("MLP Accuracy Testing %.3f" %(MLP_test_ACC))

# XXX
# TODO: Test its accuracy on the training set using the accuracy_score method.
# TODO: Test its accuracy on the test set using the accuracy_score method.
# XXX



# ############################################### Random Forest Classifier ##############################################
# XXX
# TODO: Create a RandomForestClassifier and train it.
# XXX
RF = RandomForestClassifier()
RF.fit(X_train, y_train)

RF_train_predict = RF.predict(X_train)
RF_train_ACC = accuracy_score(y_train, RF_train_predict)

RF_test_predict = RF.predict(X_test)
RF_test_ACC = accuracy_score(y_test, RF_test_predict)

print("RF Accuracy Training %.3f" %(RF_train_ACC))
print("RF Accuracy Testing %.3f" %(RF_test_ACC))
# XXX
# TODO: Test its accuracy on the training set using the accuracy_score method.
# TODO: Test its accuracy on the test set using the accuracy_score method.
# XXX

# XXX
# TODO: Tune the hyper-parameters 'n_estimators' and 'max_depth'.
#       Print the best params, using .best_params_, and print the best score, using .best_score_.
# XXX
params = {'n_estimators':[30, 50, 80, 100], 'max_depth':[1,3,5,7,9]}
grid_RF = GridSearchCV(RF, params, cv=10)
grid_RF.fit(X_train, y_train)

print("Random Forest Best Parameters: " + str(grid_RF.best_params_))
print("Random Forest Best Score: " + str(grid_RF.best_score_))

RF_grid_test_predict = grid_RF.predict(X_test)
RF_grid_test_ACC = accuracy_score(y_test, RF_grid_test_predict)
print("RF Tuned Accuracy Testing %.3f" %(RF_grid_test_ACC))
# ############################################ Support Vector Machine ###################################################
# XXX
# TODO: Pre-process the data to standardize or normalize it, otherwise the grid search will take much longer
# TODO: Create a SVC classifier and train it.
# XXX

X_train_p = normalize(X_train, axis=0)
X_test_p = normalize(X_test, axis=0)

# SVM = SVC(random_state=random_state, C=1, kernel='rbf')
SVM = SVC()
SVM.fit(X_train_p, y_train)

# XXX
# TODO: Test its accuracy on the training set using the accuracy_score method.
# TODO: Test its accuracy on the test set using the accuracy_score method.
# XXX
SVM_train_predict = SVM.predict(X_train_p)
SVM_train_ACC = accuracy_score(y_train, SVM_train_predict)

SVM_test_predict = SVM.predict(X_test_p)
SVM_test_ACC = accuracy_score(y_test, SVM_test_predict)

print("SVM Accuracy Training %.3f" %(SVM_train_ACC))
print("SVM Accuracy Testing %.3f" %(SVM_test_ACC))
# XXX
# TODO: Tune the hyper-parameters 'C' and 'kernel' (use rbf and linear).
#       Print the best params, using .best_params_, and print the best score, using .best_score_.
# XXX
params = {'C':[0.001,1,1000], 'kernel':('linear','rbf')}
SVM = SVC()
clf_SVM = GridSearchCV(SVM, params, cv=10)
tic = time.time()
clf_SVM.fit(X_train_p, y_train)

toc = time.time() - tic
print("SVM Best Parameters: " + str(clf_SVM.best_params_))
print("SVM Forest Best Score: " + str(clf_SVM.best_score_))
print("SVM CV Result: " + str(clf_SVM.cv_results_))
print("Fitting time: " + str(toc))
