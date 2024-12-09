import cv2
import subprocess

# RTSP 서버 URL 및 스트림 설정
rtsp_url = "rtsp://127.0.0.1:8554/webcam"

# OpenCV로 웹캠 캡처
cap = cv2.VideoCapture(0)  # 0은 기본 웹캠, 변경 가능

# ffmpeg 명령어 설정
ffmpeg_cmd = [
    "ffmpeg",
    "-y", "-f", "rawvideo", "-vcodec", "rawvideo",
    "-pix_fmt", "bgr24", "-s", "640x480", "-r", "30", "-i", "-",
    "-c:v", "libx264", "-preset", "veryfast", "-f", "rtsp", rtsp_url
]

# ffmpeg 프로세스 시작
ffmpeg_proc = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE)

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 웹캠 프레임을 ffmpeg로 전달
        ffmpeg_proc.stdin.write(frame.tobytes())
except KeyboardInterrupt:
    pass
finally:
    # 종료 처리
    cap.release()
    ffmpeg_proc.stdin.close()
    ffmpeg_proc.wait()
