import cv2
import time
from ffmpeg_streamer import Streamer

cap = cv2.VideoCapture(-1)
shape = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
streamer = Streamer("rtmp://localhost:1935/live/cap", shape)

while True:
    ret, frame = cap.read()
    if not ret:
        continue
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break    
    cv2.putText(frame, "Row Time: {}".format(time.strftime("%X")), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)
    streamer.pushframe(frame)

cap.release()