import MPcomms.RTMPVideo.streaming.VideoStreamer as VS
import numpy.typing as npt
from picamera2 import Picamera2

if __name__ == "__main__":
    resolution = (1280, 480)
    # resolution = (4056, 3040)

    cam = Picamera2()
    preview_config = cam.create_preview_configuration(
        {"format": "BGR888", "size": resolution})
    cam.configure(preview_config)
    cam.start()

    # streamer_rgb = VS.VideoStreamer('rgb')

    # streamer_rgb.run()

    try:
        while True:
            img_rgb : npt.ArrayLike = cam.capture_buffer()
            print(img_rgb)
            # streamer_rgb.publishFrame(img_rgb)
    except Exception as e:
        # streamer_rgb.close()
        print(e)
