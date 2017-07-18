/*
 * test_slic.cpp.
 *
 * Written by: Pascal Mettes.
 *
 * This file creates an over-segmentation of a provided image based on the SLIC
 * superpixel algorithm, as implemented in slic.h and slic.cpp.
 */
 
#include <opencv/cv.h>
#include <opencv/highgui.h>
#include <stdio.h>
#include <math.h>
#include <vector>
#include <float.h>

#include "opencv/cv.h"
#include <opencv2/highgui/highgui.hpp>
using namespace std;
using namespace cv;

#include "slic.h"

int main(int argc, char *argv[]) {
    /* Load the image and convert to Lab colour space. */
    IplImage *image = cvLoadImage(argv[1], 1);
    IplImage *lab_image = cvCloneImage(image);
    cvCvtColor(image, lab_image, CV_BGR2Lab);
    
    /* Yield the number of superpixels and weight-factors from the user. */
    int w = image->width, h = image->height;
    int nr_superpixels = atoi(argv[2]);
    int nc = atoi(argv[3]);

    double step = sqrt((w * h) / (double) nr_superpixels);
    
    /* Perform the SLIC superpixel algorithm. */
    Slic slic;
    slic.generate_superpixels(lab_image, step, nc);
    slic.create_connectivity(lab_image);
    
    /* Display the contours and show the result. */
    slic.display_contours(image, CV_RGB(255,0,0));

    //To display contour indices
    Mat img=Mat(image->height,image->width,CV_8UC3, Scalar(0,0,0));
    Mat img1=imread("/home/aritra/final.png",0);

    for(int i=0;i< image->height;i++)
        for(int j=0;j<image->width;j++)
            img.at<Vec3b>(i,j)={(100*slic.clusters[j][i]/2)%255, (100*slic.clusters[j][i])%255, (100*slic.clusters[j][i]/4)%255};

    int **clus;
    clus=(int**)malloc(image->height*sizeof(int*));
    
    for(int i=0;i<image->height;i++)
    {
    	clus[i]=(int*)malloc(image->width*sizeof(int));

    }
    
    for(int i=0;i<image->height;i++)
    {
    	for(int j=0;j<image->width;j++)
    	{
             clus[i][j]=slic.clusters[j][i];
          
    	}
    }    

    int max=-1000,min=1000;

    for(int i=0;i<image->height;i++)
    {
    	for(int j=0;j<image->width;j++)
    	{
    		if(clus[i][j]>max)
    		{
    			max=clus[i][j];
    		}
    		if(clus[i][j]<min)
    		{
    			min=clus[i][j];
    		}
    	}
    }

    int black,white,temp;

    for(int k=min;k<=max;k++)
    {
    	black=0;
    	white=0;
    	for(int i=0;i<image->height;i++)
    	{
    		for(int j=0;j<image->width;j++)
    		{
    			if(slic.clusters[j][i]==k)
    			{
    				if(img1.at<uchar>(i,j)==255)
    				{
    					white++;
    				}
    				else
    				{
    					black++;
    				}
    			}
    		if(white>=black)
    		{
    			temp=1;
    		}	
    		else
    		{
    			temp=0;
    		}

    		}
    	}

    	for(int i=0;i<image->height;i++)
    	{
    		for(int j=0;j<image->width;j++)
    		{
    			if(slic.clusters[j][i]==k)
    			{
    				if(temp==1)
    				{
    					img1.at<uchar>(i,j)=255;
    				}
    				else
    				{
    					img1.at<uchar>(i,j)=0;
    				}
    			}
    		}
    	}


    }
    namedWindow("clus",WINDOW_AUTOSIZE);
    imshow("clus",img1);

    //imshow("clusters :)", img);  


    cvShowImage("result", image);
    cvWaitKey(0);
    cvSaveImage(argv[4], image);
}
