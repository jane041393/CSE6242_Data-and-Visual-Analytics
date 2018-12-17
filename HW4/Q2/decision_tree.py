from util import entropy, information_gain, partition_classes
import numpy as np 
import ast

class DecisionTree(object):
    def __init__(self):
        # Initializing the tree as an empty dictionary or list, as preferred
        #self.tree = []
        #self.tree = {}
        self.tree = [-1, 'attr', 'left', 'right']

    def learn(self, X, y):
        # TODO: Train the decision tree (self.tree) using the the sample X and labels y
        # You will have to make use of the functions in utils.py to train the tree
        
        # One possible way of implementing the tree:
        #    Each node in self.tree could be in the form of a dictionary:
        #       https://docs.python.org/2/library/stdtypes.html#mapping-types-dict
        #    For example, a non-leaf node with two children can have a 'left' key and  a 
        #    'right' key. You can add more keys which might help in classification
        #    (eg. split attribute and split value)
        data_length = range(len(X[0]))
        def _learn(X, y):
            Y_entropy = entropy(y)
            if Y_entropy == 0:
                return [-1, y[0], None, None]

            cur_max_gain = 0
            best_attr = []
            best_index = -1

            for index in data_length:

                if type(X[0][index]) == str:
                    is_str = True
                else:
                    is_str = False
                if is_str == True:
                    attr_X = np.unique([X[i][index] for i in range(len(X))])
         
                    for attr in attr_X:
                        X_left, X_right, y_left, y_right = partition_classes(X, y , index, attr)
                        gain = information_gain(y, [y_left, y_right] )
                        if gain > cur_max_gain:
                            cur_max_gain = gain
                            best_index = index
                            best_attr = attr
                            best_X_left, best_X_right = X_left, X_right
                            best_y_left, best_y_right = y_left, y_right
                else:                         
                    attr_X = np.mean([X[i][index] for i in range(len(X))])
                    X_left, X_right, y_left, y_right = partition_classes(X, y, index, attr_X)
                    gain = information_gain(y,[y_left,y_right])
                    if gain > cur_max_gain:
                        cur_max_gain = gain
                        best_index = index
                        best_attr = attr_X
                        best_X_left, best_X_right = X_left, X_right
                        best_y_left, best_y_right = y_left, y_right
            
            if cur_max_gain <= 0:
                return [-1,np.argmax(np.bincount(y)),None,None]

            left = _learn(best_X_left, best_y_left)
            right = _learn(best_X_right, best_y_right)

            return [ best_index, best_attr,left ,right ]
        self.tree = _learn(X, y)

    def classify(self, record):
        def _classify(record, tree):
            index, attr, left, right = tree
            if index == -1:
                return attr
            if type(attr) == str:
                is_str = True
            else:
                is_str = False
            if is_str:
                if record[index] == attr:
                    return _classify(record, left)
                else:
                    return _classify(record, right)
            else:
                if record[index] <= attr:
                    return _classify(record, left)
                else:
                    return _classify(record, right)
        return _classify(record, self.tree)
        
 # TODO: classify the record using self.tree and return the predicted label

