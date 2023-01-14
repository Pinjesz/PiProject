import MPcomms.RTMPVideo.streaming.VideoStreamer as VS
import numpy.typing as npt
import numpy as np
import sys
from picamera2 import Picamera2

if __name__ == "__main__":
    args = sys.argv
    if (len(args) < 3):
        resolution = (1280, 480)
    else:
        resolution = (args[1], args[2])

    cam = Picamera2()
    preview_config = cam.create_preview_configuration(
        {"format": "BGR888", "size": resolution})
    cam.configure(preview_config)
    cam.start()

    streamer_rgb = VS.VideoStreamer('rgb')

    streamer_rgb.run()

    try:
        while True:
            buffer : npt.NDArray = cam.capture_buffer()
            frame = np.zeros((resolution[1], resolution[0], 3), np.uint8)
            frame[:,:,2] = np.reshape(buffer[0::3], (resolution[1], resolution[0]))
            frame[:,:,1] = np.reshape(buffer[1::3], (resolution[1], resolution[0]))
            frame[:,:,0] = np.reshape(buffer[2::3], (resolution[1], resolution[0]))
            streamer_rgb.publishFrame(frame)
            print(np.mean(frame))
    except Exception as e:
        streamer_rgb.close()
        print(e)
