import cv2
import numpy as np
from sklearn.cluster import KMeans

img=cv2.imread("/home/aritra/transform.jpg",1)
size=np.shape(img) 
a=np.zeros((size[0]*size[1], 5))

iter=0
for i in range(0,size[0]):
	for j in range(0, size[1]):
		a[iter]=np.array([i, j, img[i,j][0], img[i,j][1], img[i,j][2]])
		iter=iter+1

kmeans=KMeans(n_clusters=5, random_state=0)
kmeans.fit(a)

out=np.zeros((size[0], size[1],3))
for i in range (0,size[0]):
	for j in range (0,size[1]):
		if kmeans.predict([[i, j, img[i,j][0], img[i,j][1], img[i,j][2]]])[0]==0:
			out[i,j,0]=255
			out[i,j,1]=0
			out[i,j,2]=0
		elif kmeans.predict([[i, j, img[i,j][0], img[i,j][1], img[i,j][2]]])[0]==1:
			out[i,j,0]=0
			out[i,j,1]=255
			out[i,j,2]=0
		elif kmeans.predict([[i, j, img[i,j][0], img[i,j][1], img[i,j][2]]])[0]==2:
			out[i,j,0]=0
			out[i,j,1]=0
			out[i,j,2]=255
		elif kmeans.predict([[i, j, img[i,j][0], img[i,j][1], img[i,j][2]]])[0]==3:
			out[i,j,0]=255
			out[i,j,1]=255
			out[i,j,2]=255
		else:
			out[i,j,0]=125
			out[i,j,1]=125
			out[i,j,2]=0

print size[1]	

for i in range(0,size[0]):
	for j in range(160,size[1]):
		if(kmeans.predict([[i, j, img[i,j][0], img[i,j][1], img[i,j][2]]])[0]==2):
			for k in range(0,size[0]):
				img[k,j,0]=255
				img[k,j,1]=255
				img[k,j,2]=255

cv2.imshow("real",img)
cv2.imshow("seg",out)
cv2.waitKey(0)

