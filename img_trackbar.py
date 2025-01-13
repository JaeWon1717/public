import cv2
import numpy as np

# 이미지 불러오기
image_path = '/Users/jaewon/Desktop/Taskfolder/testcode/ship.png'  # 테스트할 이미지 경로 설정
image = cv2.imread(image_path)

if image is None:
    print("이미지를 불러올 수 없습니다. 경로를 확인하세요.")
    exit()

# 밝기와 대비를 조절하는 함수
def update_image(x):
    brightness = cv2.getTrackbarPos('Brightness', 'Image') - 100  # 밝기 조절 범위: -100 ~ 100
    contrast = cv2.getTrackbarPos('Contrast', 'Image') / 50.0  # 대비 조절 범위: 0.0 ~ 2.0

    # 이미지 복사
    adjusted = np.int16(image)
    adjusted = adjusted * contrast + brightness  # 이미지 조정
    adjusted = np.clip(adjusted, 0, 255)  # 픽셀 값 제한 (0 ~ 255)
    adjusted = np.uint8(adjusted)  # uint8 형 변환

    cv2.imshow('Image', adjusted)  # 이미지 출력

# 윈도우 생성
cv2.namedWindow('Image')

# 트랙바 생성 (밝기: -100 ~ 100, 대비: 0 ~ 200)
cv2.createTrackbar('Brightness', 'Image', 100, 200, update_image)  # 초기 값 100 -> 실제 밝기 0
cv2.createTrackbar('Contrast', 'Image', 50, 100, update_image)  # 초기 값 50 -> 실제 대비 1.0

# 초기 이미지 출력
update_image(0)

# 'q'를 누르면 종료
while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
