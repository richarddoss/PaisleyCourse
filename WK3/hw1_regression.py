import numpy as np
import sys

lambda_input = int(sys.argv[1])
sigma2_input = float(sys.argv[2])
X_train = np.genfromtxt(sys.argv[3], delimiter = ",")
y_train = np.genfromtxt(sys.argv[4])
X_test = np.genfromtxt(sys.argv[5], delimiter = ",")

## Solution for Part 1
def part1(X_train,y_train,X_test,lambda_input):
    ## Input : Arguments to the function
   X = np.matrix(X_train)
   Nd = X.shape
   d = Nd[1]
   y = np.matrix(y_train).T
   B=np.dot(X.T,y)
   A=np.linalg.inv(np.add(lambda_input*np.identity(d),np.dot(X.T,X)))
   wRR = np.dot(A,B)
   print(wRR)
  # Inverse= lambda_input*(np.identity(d))+ X_train'*X_train)i
    ## Return : wRR, Final list of values to write in the file
   # pass

part1(X_train,y_train,X_test,lambda_input)  # Assuming wRR is returned from the function
# print(wRR)
#np.savetxt("wRR_" + str(lambda_input) + ".csv", wRR, delimiter="\n") # write output to file


## Solution for Part 2
def part2(X_train,y_train,X_test,lambda_input,sigma2_input):
    ## Input : Arguments to the function
    X = np.matrix(X_train)
    sigmaInv=1/sigma2_input
    Nd = X.shape
    d = Nd[1]
    y = np.matrix(y_train).T
    XTX=np.dot(X.T,X)
    XTy=np.dot(X.T,y)
    lamd_i=lambda_input*np.identity(d)
    # compute co-variance matrix of the posterior distr on the weights
    eps = np.linalg.inv(np.add(lamd_i, sigmaInv*XTX))
    # compute variance for each prediction over the entire X_test
    Xtest = np.matrix(X_test)
    TestObs = Xtest.shape
    TestObs = TestObs[0]
    sigmaVal = np.zeros(50)
    print(eps.shape)
    for x in range(TestObs):
        #print(Xtest[x,:].T.shape)
        #print(Xtest[x,:].shape)
        sigmaVal[x]=sigma2_input +np.dot(np.dot( Xtest[x,:],eps),Xtest[x,:].T)
        #print(sigma0)
    print(sigmaVal)
    idx=np.argsort(sigmaVal)
    # return 10 points with the most variance to be measured for y values
    print(idx[0:10])
    #print(idx)
    ## Return : active, Final list of values to write in the file


part2(X_train,y_train,X_test,lambda_input,sigma2_input)  # Assuming active is returned from the function
#np.savetxt("active_" + str(lambda_input) + "_" + str(int(sigma2_input)) + ".csv", active, delimiter=",") # write output to file
