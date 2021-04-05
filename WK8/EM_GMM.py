import numpy as np
from scipy import stats
# load files
X = np.genfromtxt("X.csv",delimiter=",")
# init prior distribution
pi = np.random.rand(3)
mean = np.random.rand(3,3)
cov = [[1,0,0],[0,1,0],[0,0,1]]
# number of clusters
NC = 3
Weight = np.zeros((100,NC))
L = np.zeros(NC)
for i in range(100):
    # E step
    print(X[i])
    for k  in range(NC):
        var = stats.multivariate_normal(mean=mean[k],cov=cov)
        L[k] = pi[k]*var.pdf(X[i])
    sumL = sum(L)
    for k in  range(NC):
        Weight[i][k] = L[k]/sumL

print(Weight)
