import math

import cv2
import numpy as np


import cv2
import numpy as np

img_file = "./img/girl.jpg"  # 표시할 이미지 경로            ---①
img = cv2.imread(img_file)  # 이미지를 읽어서 img 변수에 할당 ---②
print(img.shape)

cv2.imshow('IMG', img)  # 읽은 이미지를 화면에 표시      --- ③
cv2.waitKey()  # 키가 입력될 때 까지 대기      --- ④
cv2.destroyAllWindows()  # 창 모두 닫기            --- ⑤

imgy = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

y, u, v = cv2.split(imgy)
print(y.shape)
# cv2.imshow("IMG2", y)
# cv2.waitKey()  # 키가 입력될 때 까지 대기      --- ④
# cv2.destroyAllWindows()  # 창 모두 닫기

import numpy as np
imgmyy = np.full((293, 406), 255, dtype=np.uint8)
b, g, r = cv2.split(img)
imgmyy = (b * 0.114) + (g * 0.587) + (r * 0.299)
imgmyy = imgmyy.astype(int)
print(f'{imgmyy.shape}')
print(imgmyy)
print(y)
imyy = imgmyy.copy()
cv2.imshow("YUV", imyy)

cv2.imshow("IMG2", y)
cv2.waitKey()  # 키가 입력될 때 까지 대기      --- ④
cv2.destroyAllWindows()  # 창 모두 닫기