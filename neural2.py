import cv2
from sklearn.neural_network import MLPClassifier 
import numpy as np

img_train=cv2.imread("/home/aritra/train.png",1)

img_test=cv2.imread("/home/aritra/test.png",1)

size=np.shape(img_test)
#a=np.zeros((size[0]*size[1],5))
#b=np.zeros((size[0]*size[1],))

#print size[0]*size[1]
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
#cv2.imshow("train",img_train)
#cv2.imshow("test",img_test)

out=np.zeros((size[0],size[1],3))

io=0
jo=0
thi=50
thj=50
temp=1
count=0

for i in range(0,size[0]):
	for j in range(0,size[1]):
		out[i,j,0]=255
		out[i,j,1]=0
		out[i,j,2]=0


while temp==1:
	iter=0
	count=count+1
	print count
	a=np.zeros((size[0]*size[1],5))

	b=np.zeros((size[0]*size[1],))

	for i in range(io,io+thi):
		for j in range(jo,jo+thj):
			a[iter]=np.array([i,j,img_test[i,j][0],img_test[i,j][1],img_test[i,j][2]])
			if img_train[i,j][0]==255:
				b[iter]=np.array(1)
			else:
			 	b[iter]=np.array(0)
			iter=iter+1
	clf=MLPClassifier(solver="lbfgs",alpha=1e-5,hidden_layer_sizes=(5,3),random_state=1,max_iter=2000)

	clf.fit(a,b)

	for i in range(io,io+thi):
		for j in range(jo,jo+thj):
			if clf.predict([[i,j,img_test[i,j][0],img_test[i,j][1],img_test[1,j][2]]])==0:
				out[i,j,0]=0
				out[i,j,1]=0
				out[i,j,2]=0
			else:
				out[i,j,0]=255
				out[i,j,1]=255
				out[i,j,2]=255

	jo=jo+50
	thi=50
	thj=50

	del a
	
	del b

	if  jo+50>=size[1] & jo<size[1]:
		thj=size[1]-jo

	if  io+50>=size[0] & io<size[0]:
		thi=size[0]-io

	if io>size[0] & jo>size[1]:
	 	break

	if jo>=size[1]:
		io=io+50
		jo=0		

     

cv2.imshow("neural2",out)
cv2.waitKey(0)    			

			   


