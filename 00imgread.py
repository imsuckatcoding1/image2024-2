import cv2


img_file = "./img/girl.jpg"
img = cv2.imread(img_file)

if img is not None:
    cv2.imshow('IMG', img)
    cv2.waitKey()  # 키가 입력될 때 까지 대기      --- ④
    cv2.destroyAllWindows()  # 창 모두 닫기            --- ⑤
else:
    print('No image file.')

# >pip install pillow
from PIL import Image
img = Image.open("./img/girl.jpg")
img.show()

#이미지파일 그레이로 읽기
img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)  # 이미지를 읽어서 img 변수에 할당 ---②

if img is not None:
    cv2.imshow('IMG', img)  # 읽은 이미지를 화면에 표시      --- ③
    cv2.waitKey()  # 키가 입력될 때 까지 대기      --- ④
    cv2.destroyAllWindows()  # 창 모두 닫기            --- ⑤
else:
    print('No image file.')

# 동영상파일 읽기
video_file = "./img/big_buck.avi" # 동영상 파일 경로

cap = cv2.VideoCapture(video_file) # 동영상 캡쳐 객체 생성  ---①
if cap.isOpened():                 # 캡쳐 객체 초기화 확인
    while True:
        ret, img = cap.read()      # 다음 프레임 읽기      --- ②
        if ret:                     # 프레임 읽기 정상
            cv2.imshow(video_file, img) # 화면에 표시  --- ③
            cv2.waitKey(25)            # 25ms 지연(40fps로 가정)   --- ④
        else:                       # 다음 프레임 읽을 수 없슴,
            break                   # 재생 완료
else:
    print("can't open video.")      # 캡쳐 객체 초기화 실패
cap.release()                       # 캡쳐 자원 반납
cv2.destroyAllWindows()

# 비디오카메라 읽기
cap = cv2.VideoCapture(0)               # 0번 카메라 장치 연결 ---①
if cap.isOpened():                      # 캡쳐 객체 연결 확인
    while True:
        ret, img = cap.read()           # 다음 프레임 읽기
        if ret:
            cv2.imshow('camera', img)   # 다음 프레임 이미지 표시
            if cv2.waitKey(1) != -1:    # 1ms 동안 키 입력 대기 ---②
                break                   # 아무 키라도 입력이 있으면 중지
        else:
            print('no frame')
            break
else:
    print("can't open camera.")
cap.release()                           # 자원 반납
cv2.destroyAllWindows()

# 사진찍기

cap = cv2.VideoCapture(0)                       # 0번 카메라 연결
if cap.isOpened() :
    while True:
        ret, frame = cap.read()                 # 카메라 프레임 읽기
        if ret:
            cv2.imshow('camera',frame)          # 프레임 화면에 표시
            if cv2.waitKey(1) != -1:            # 아무 키나 누르면
                cv2.imwrite('./img/photo.jpg', frame) # 프레임을 'photo.jpg'에 저장
                break
        else:
            print('no frame!')
            break
else:
    print('no camera!')
cap.release()
cv2.destroyAllWindows()