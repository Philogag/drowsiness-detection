### 容器封装使用手册

1. 使用 `docker-compose up -d` 安装启动容器组.
2. 运行 `python3 cam_streamer.py` 推流摄像头
3. 浏览器打开 http://localhost:8080/players2/index.html 查看流

> cam_streamer运行于容器组外，需要 opencv-python 库, 以及 ffmpeg

流配置:

+ 推流地址：`rtmp://<ip>:<port>/live/<room-id>`
+ 接收流地址
    + rtmp协议(cv2接收): 同推流地址
    + hls协议(网页查看用): `/hls/<room-id>.m3u8`

摄像头流id: `cap`  
检测后输出id: `detect`

### 架构图

![](/player/struct.png)
