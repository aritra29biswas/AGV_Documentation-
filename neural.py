import cv2
from sklearn.neural_network import MLPClassifier 
import numpy as np

img_train=cv2.imread("/home/aritra/train.png",1)

img_test=cv2.imread("/home/aritra/test.png",1)

size=np.shape(img_test)
a=np.zeros((size[0]*size[1],5))
b=np.zeros((size[0]*size[1],))

print size[0]*size[1]
for i in range (0,size[0]):
	for j in range(0,size[1]):
		if img_train[i,j][0]==0:
			img_train[i,j][0]=0
			img_train[i,j][1]=0
			img_train[i,j][2]=255
		else:
			img_train[i,j][0]=255
			img_train[i,j][1]=0
			img_train[i,j][2]=0
cv2.imshow("train",img_train)
cv2.imshow("test",img_test)
iter=0
for i in range(0,size[0]):
	for j in range(0,size[1]):
		a[iter]=np.array([i,j,img_test[i,j][0],img_test[i,j][1],img_test[i,j][2]])
		iter=iter+1

iter=0
for i in range(0,size[0]):
	for j in range(0,size[1]):
		if img_train[i,j][0]==255:
			b[iter]=np.array(1)
		else:
			b[iter]=np.array(0)
		iter=iter+1	
clf=MLPClassifier(solver="lbfgs",alpha=1e-5,hidden_layer_sizes=(5,3),random_state=1,max_iter=2000)

clf.fit(a,b)

#MLPClassifier(activation='relu',alpha=1e-5,batch_size='auto',beta_1=0.9,beta_2=0.990,early_stopping=False,epsilon=1e-08,hidden_layer_sizes=(5,3,3),learning_rate='constant',learning_rate_inti=0.001,max_iter=200,momentum=0.9,nesterovs_momentum=True,power_t=0.5,random_state=1,shuffle=True,solver='lbfgs',tol=0.0001,validation_fraction=0.1,verbose=False,warm_start=False)

out=np.zeros((size[0],size[1],3))

for i in range(0,size[0]):
	for j in range(0,size[1]):
		if clf.predict([[i,j,img_test[i,j][0],img_test[i,j][1],img_test[1,j][2]]])==0:
			out[i,j,0]=0
			out[i,j,1]=0
			out[i,j,2]=0
		else:
			out[i,j,0]=255
			out[i,j,1]=255
			out[i,j,2]=255

#		print clf.predict([[i,j,img_test[i,j][0],img_test[i,j][1],img_test[1,j][2]]])	

cv2.imshow("neural",out)			

#print clf.predict([[3,3,img_test[3,3][0],img_test[3,3][1],img_test[3,3][2]]])
cv2.waitKey(0)