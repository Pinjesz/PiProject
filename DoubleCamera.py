import cv2
import MPcomms.RTMPVideo.streaming.VideoStreamer as VS
from MPcomms.RTMPVideo.DummyCap import DummyCap as DCap
from picamera2 import Picamera2

if __name__ == "__main__":
    resolution = (3840, 1080)
    # resolution = (4056, 3040)

    cam = Picamera2()
    preview_config = cam.create_preview_configuration({"format": "BGR888", "size": resolution})
    cam.configure(preview_config)
    cam.start()

    streamer_rgb = VS.VideoStreamer('rgb')

    streamer_rgb.run()

    while True:
        img_rgb = cam.capture_buffer()

        # img_gs = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

        streamer_rgb.publishFrame(img_rgb)

        # cv2.imshow('streamer', img_rgb)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

    streamer_rgb.close()
