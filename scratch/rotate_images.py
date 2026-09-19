from PIL import Image
import os

d_dir = r"C:\Users\그램\Desktop\입시분석 참고자료\논술일정표"
img1 = Image.open(os.path.join(d_dir, "KakaoTalk_20260809_133628902_01.jpg"))
img1.rotate(180, expand=True).save("scratch/nonsul_01_rot.jpg")

img2 = Image.open(os.path.join(d_dir, "KakaoTalk_20260809_133628902_02.jpg"))
img2.rotate(180, expand=True).save("scratch/nonsul_02_rot.jpg")

print("ROTATED_SUCCESSFULLY")
