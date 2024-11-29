import cv2
import os

# 동영상 파일 경로와 저장할 이미지 폴더 경로 설정
video_path = '/Users/jaewon/Desktop/labeling_opencv/10-30-2024_08_27_52_PM.labeling.mov'
output_folder = '/Users/jaewon/Desktop/labeling_opencv/10-30-2024_08_27_52_PM.labeling'

# 출력 폴더가 없으면 생성
os.makedirs(output_folder, exist_ok=True)

# 동영상 파일 열기
cap = cv2.VideoCapture(video_path)

# 동영상의 프레임 속도(fps) 얻기
fps = cap.get(cv2.CAP_PROP_FPS)

# 1초 간격의 프레임 수 계산
frame_interval = int(fps)  # 1초마다 1프레임 추출

frame_count = 0
saved_image_count = 0

while cap.isOpened():
    # 프레임 읽기
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # 1초 간격으로 프레임을 저장
    if frame_count % frame_interval == 0:
        image_path = os.path.join(output_folder, f'cam_front_{saved_image_count}.jpg')
        cv2.imwrite(image_path, frame)
        print(f'Saved: {image_path}')
        saved_image_count += 1
    
    frame_count += 1

# 동영상 파일 닫기
cap.release()
print("Frames have been extracted and saved.")
