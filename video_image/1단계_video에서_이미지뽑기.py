# Importing all necessary libraries
import cv2
import os

# Read the video from specified path
cam = cv2.VideoCapture("C:\\Users\\user\\Desktop\\fired3.mp4")

try:

    # creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')

# if not created then raise error
except OSError:
    print ('Error: Creating directory of data')

# frame
currentframe = 0


while(cam.isOpened()):
    ret, image = cam.read()
#만약 30초짜리 영상이고 30프레임짜라면 총 프레임은 900, 따라서 만약 %100해주면 전체프레임의  1/100의  프레임만 가져옴, 즉 9장의 이미지만 가져옴
#동영상 프레임 확인은 마우스오른쪽->속성->자세히->프레임속도 이 부분 보면 됨
    if(int(cam.get(1)) % 4 == 0):
        print('Saved frame number : ' + str(int(cam.get(1))))
        cv2.imwrite("frame%d.jpg" %currentframe, image)
        print('Saved frame%d.jpg' % currentframe)
        currentframe += 1

cam.release()

cv2.destroyAllWindows()
