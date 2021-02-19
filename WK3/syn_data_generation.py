import numpy as np
# create 1000 train and 50 test
X = np.random.random_sample((1050,3))
print(X[0,:])
Y = 2*X[:,0]+3*X[:,1]
ytrain = Y[0:1000]
xtrain = X[0:1000,:]
xtest = X[1000:1050,:]
ytest = Y[1000:1050]
np.savetxt("xtrain.csv",xtrain,delimiter=",",newline='\n')
np.savetxt("ytrain.csv",ytrain,delimiter=",",newline="\n")
np.savetxt("xtest.csv",xtest,delimiter=",",newline="\n")
np.savetxt("ytest.csv",ytest,delimiter=",",newline="\n")





