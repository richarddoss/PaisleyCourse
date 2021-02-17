import numpy as np
# create 1000 train and 50 test
X = np.random.random_sample((1050,3))
print(X[0,:])
Y = 2*X[:,0]+3*X[:,1]
ytrain = Y[0:1001]
xtrain = X[0:1001,:]
xtest = X[1001:1051,:]
ytest = Y[1001:1051]
np.savetxt("xtrain.csv",xtrain,delimiter=",",newline='\n')
