import cv2
import numpy as np

img = cv2.imread('./img/sunset.jpg')

x=320; y=150; w=50; h=50

cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255,0))
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# roi 지정후 프로그램

roi=img[y:y+h, x:x+w]
print(roi.shape)
cv2.rectangle(roi, (0,0), (h-1, w-1), (0,255,0))
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread('./img/sunset.jpg')
roi=img[y:y+h, x:x+w]
img2 = roi.copy()
img[y:y+h, x+w:x+w+w] = roi
cv2.rectangle(img, (x,y), (x+w+w, y+h ), (0, 255,0))
cv2.imshow("img", img)
cv2.imshow("roi", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()



x,y,w,h	=	cv2.selectROI('img', img, False)
if w and h:
    roi = img[y:y+h, x:x+w]
    cv2.imshow('cropped', roi)  # ROI 지정 영역을 새창으로 표시
    cv2.moveWindow('cropped', 0, 0) # 새창을 화면 좌측 상단에 이동
    cv2.imwrite('./cropped2.jpg', roi)   # ROI 영역만 파일로 저장

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()