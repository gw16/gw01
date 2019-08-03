#쥬피터노트북에서 실행하면 됨.
import os
import glob
os.chdir("C:/Users/user/Desktop/video_cap/화재영상2_전봇대발화")
a= glob.glob("*.*")
for i in a:
    b= i.split(".")
    b[1]="jpg"
    c=".".join(b)
    os.rename(i,c)

#현재 디렉토리검색
os.getcwd()



#사이즈 조절 처리후 저장
from PIL import Image
import os
import glob
from PIL import ImageFilter

os.chdir("C:/Users/user/Desktop/video_cap/화재영상2_전봇대발화")
try:

    glob.glob("*.*")
    for i in glob.glob("*.*"):
        image = Image.open(i)
        image.convert('RGB')
        resize= image.resize((800,600))
        resize.save('1'+i)
except OSError:
    pass
