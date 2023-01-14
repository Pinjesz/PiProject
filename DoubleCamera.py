import MPcomms.RTMPVideo.streaming.VideoStreamer as VS
import numpy.typing as npt
import numpy as np
from picamera2 import Picamera2

if __name__ == "__main__":
    resolution = (1280, 480)
    # resolution = (4056, 3040)

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
            frame[:,:,1] = np.transpose(np.reshape(buffer[0::3], (resolution[0], resolution[1])))
            frame[:,:,2] = np.transpose(np.reshape(buffer[1::3], (resolution[0], resolution[1])))
            frame[:,:,3] = np.transpose(np.reshape(buffer[2::3], (resolution[0], resolution[1])))
            streamer_rgb.publishFrame(frame)
    except Exception as e:
        streamer_rgb.close()
        print(e)
