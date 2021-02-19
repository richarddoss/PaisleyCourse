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
   print(d)
  # np.multiply(X.T,X)
   y = np.matrix(y_train).T
   print(y.shape)
   B=np.dot(X.T,y)
   A=np.linalg.inv(np.add(lambda_input*np.identity(d),np.dot(X.T,X)))
   print(A.shape)
   print(B.shape)
   wRR = np.dot(A,B)
   print(wRR)
  # Inverse= lambda_input*(np.identity(d))+ X_train'*X_train)i
    ## Return : wRR, Final list of values to write in the file
   # pass

part1(X_train,y_train,X_test,lambda_input)  # Assuming wRR is returned from the function
# print(wRR)
#np.savetxt("wRR_" + str(lambda_input) + ".csv", wRR, delimiter="\n") # write output to file


## Solution for Part 2
#def part2():
    ## Input : Arguments to the function
    ## Return : active, Final list of values to write in the file
#    pass

#active = part2()  # Assuming active is returned from the function
#np.savetxt("active_" + str(lambda_input) + "_" + str(int(sigma2_input)) + ".csv", active, delimiter=",") # write output to file
