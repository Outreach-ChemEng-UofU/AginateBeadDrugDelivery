# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 08:41:53 2018

@author: tony butterfield
"""
# STUFF I WANNA USE 
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from skimage.filters import threshold_minimum,threshold_otsu
from skimage.measure import label, regionprops
from skimage.morphology import closing, square
from skimage.color import label2rgb
from skimage.segmentation import clear_border

plt.close('all')  #close all open plots, start fresh

####    YOU MUST CHANGE THE PATH STRING BELOW TO LOAD YOUR BEAD PHOTO     ####
#########################################################################
I = sp.misc.imread("D:\GoogleDrive\Python\CHEN 1705\AlginateBead\sample3.jpg")
##########################################################################

Ir = I.copy() #red channel
Ir[:,:,1]=0  #Image files are 3 D matrix where  0 = red, 1 = green, 2 = blue
Ir[:,:,2]=0
Ig = I.copy() #green channel, really all we need but want to show you diff
Ig[:,:,0]=0 # set reds to zero
Ig[:,:,2]=0 # set blues to zero
Ib = I.copy()  #blue channel
Ib[:,:,0]=0
Ib[:,:,1]=0

f, ax = plt.subplots(2, 2) #create a 2 x 2 set of subplots (4 total)
ax[0,0].set_title('Raw Img') #set the figure title
ax[0,0].imshow(I)  #show the image
ax[0,0].axis('off') #images need no axis
ax[0,1].set_title('Red Channel') #set the title for red
ax[0,1].imshow(Ir)
ax[0,1].axis('off')
ax[1,0].set_title('Green Channel') #set the title for green
ax[1,0].imshow(Ig)
ax[1,0].axis('off')
ax[1,1].set_title('Blue Channel') #set the title for blue
ax[1,1].imshow(Ib)
ax[1,1].axis('off')

Igg=I.copy() #goind to make BW img out of green channel
Igg[:,:,0]=Igg[:,:,1]  #red and blue get same values as green channel
Igg[:,:,2]=Igg[:,:,1]
f, ax = plt.subplots(2, 2) # make another 2x2 plot
ax[0,0].imshow(Igg)  #show gray scale image of green channel
ax[0,0].axis('off')
ax[0,0].set_title('Green Channel, BW')

#### YOU MIGHT NEED TO CHANGE THE THRESHOLD BELOW TO PICK OUT FROM NOISE   ####
#### AND IGNORE SHADOWS. HIGHER VALUES MEANS MORE GRAYS WILL BE MADE BLACK ####
