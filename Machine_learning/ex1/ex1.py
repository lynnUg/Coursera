import numpy as np
def computeCost(X,y,theta):
    m=np.size(y)
    hypo=X*theta
    error=np.squares(X-y)
    J=1/float(2*m)*np.sum(error)
    
def main :
    txt_file_object=csv.reader(open('ex1data1.txt','rb'))
    train_data=[]
    for row in txt_file_object:
        train_data.append(row)
    train_data=np.matrix(train_data)
    train_data=train_data.astype(np.float)
    train_data=numpy.hstack((numpy.zeros((train_data.shape[0], 1)), train_data))

    theta = np.matrix( ((-3.878051), (1.191253)) )
    theta=theta.reshape(-1,1)
    X=train_data[0::,:2]
    y=train_data[0::,2]
