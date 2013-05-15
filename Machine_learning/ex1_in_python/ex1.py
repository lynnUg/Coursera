import numpy as np
import csv
def gradientDescent(X,y,theta,alpha,num_iters):
    m=np.size(y)
    J_history=np.zeros(num_iters)
    for iter in range(0,num_iters):
        hypo=X*theta
        error=(hypo-y)
        theta=theta-alpha*(1/float(m))* ( X.conj().transpose()*error)
        J_history[iter]=computeCost(X,y,theta)
    print J_history
def computeCost(X,y,theta):
    m=np.size(y)
    hypo=X*theta
    error=np.square(hypo-y)
    J=1/float(2*m)*np.sum(error)
    print J
    
def main() :
    txt_file_object=csv.reader(open('ex1data1.txt','rb'))
    train_data=[]
    for row in txt_file_object:
        train_data.append(row)
    train_data=np.matrix(train_data)
    train_data=train_data.astype(np.float)
    train_data=np.hstack((np.ones((train_data.shape[0], 1)), train_data))

    theta = np.matrix( ((-3.878051), (1.191253)) )
    theta=theta.reshape(-1,1)
    X=train_data[0::,:2]
    y=train_data[0::,2]
    iterations = 10
    alpha = 0.01
    computeCost(X,y,theta)
    gradientDescent(X,y,theta,alpha,iterations)
if __name__ == '__main__':
    main()
