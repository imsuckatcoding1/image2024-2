import cv2
import numpy as np
img= np.full(shape=(500,500,3), fill_value=255,dtype=np.uint8)

cv2.putText(img,text="Plain", org=(50,30), cv2.FONT_HERSHEY_PLAIN, fontScale=1,color=(0,0,0))