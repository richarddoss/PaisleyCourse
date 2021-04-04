from scipy import stats
import numpy as np
# 3 class problem with a fixed prior of 0.2,0.5,0.3
# 3 variable gaussian problem
# mean = [1 1 1], variance=ones(3)
# mean = [2 2 2], variance=2*ones(3)
# mean = [3 3 3], variance=3*ones(3)
pk = (0.2,0.5,0.3)
mean1 = (1,1,1)
mean2 = (2,2,2)
mean3 = (3,3,3)
cov = ((1,0,0) ,(0,1,0) ,(0,0,1))
xk = np.arange(3)
custm = stats.rv_discrete(name='custm',values = (xk,pk))
y = custm.rvs(size=100)
X = np.zeros((100,3))
for i in range(100):
    cluster = y[i]
    if cluster == 0:
     X[i,:]=np.random.multivariate_normal(mean1,cov)
    if cluster == 1:
     X[i,:]=np.random.multivariate_normal(mean2,cov)
    if cluster == 2:
     X[i,:] = np.random.multivariate_normal(mean3,cov)

np.savetxt("X.csv",X,delimiter=",",newline='\n')
np.savetxt("y.csv",y,delimiter=",",newline='\n')





