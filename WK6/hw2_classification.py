from __future__ import division
import numpy as np
import pandas as pd
data = pd.read_csv('iris.data',header=None,sep=",")
data.columns = ['X1','X2','X3','X4','y']
X = data[{'X1','X2','X3','X4'}]
X=X.to_numpy()
y = np.concatenate((np.ones((50,1)),2*np.ones((50,1)),3*np.ones((50,1))))
# split data into training and test
# generate random indices
training_idx = np.random.choice(150,size=100,replace=False)
all_idx = np.array(range(150))
test_idx = np.delete(all_idx,training_idx)
X_train = X(trainin)
print(X.shape)
print(y.shape)
#X_train = np.genfromtxt(sys.argv[1], delimiter=",")
#y_train = np.genfromtxt(sys.argv[2])
#X_test = np.genfromtxt(sys.argv[3], delimiter=",")

## can make more functions if required


#def pluginClassifier(X_train, y_train, X_test):
  # this function returns the required output
#  pass


#final_outputs = pluginClassifier(X_train, y_train, X_test) # assuming final_outputs is returned from function

#np.savetxt("probs_test.csv", final_outputs, delimiter=",") # write output to file
