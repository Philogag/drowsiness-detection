
import subprocess

class Streamer():
    def __init__(self, rtmp, size):
        print("Output Size: {}x{}".format(size[0], size[1]))
        self.command = ['ffmpeg',
            '-y', '-an',
            '-f', 'rawvideo',
            '-vcodec','rawvideo',
            '-pix_fmt', 'bgr24',
            '-s', "{}x{}".format(size[0], size[1]),
            '-r', '25',
            '-i', '-',
            '-c:v', 'libx264',
            '-pix_fmt', 'yuv420p',
            '-preset', 'ultrafast',
            '-f', 'flv',
            rtmp]
        
        self.pipe = subprocess.Popen(self.command
            , shell=False
            , stdin=subprocess.PIPE
        )

    def __del__(self):
        self.pipe.terminate()
    
    def pushframe(self, frame):
        if self.pipe:
            self.pipe.stdin.write(frame.tostring())