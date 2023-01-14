import MPcomms.RTMPVideo.streaming.VideoStreamer as VS
import numpy.typing as npt
import numpy as np
import sys
from picamera2 import Picamera2


def main(resolution: list = (640, 480), camera_choose: str = 'b'):
    left = True
    right = True
    if camera_choose == 'l':
        right = False
        print(f"Left camera, resolution: {resolution[0]} x {resolution[1]}")
    elif camera_choose == 'r':
        left = False
        print(f"Right camera, resolution: {resolution[0]} x {resolution[1]}")
    else:
        print(f"Both cameras, resolution: {resolution[0]} x {resolution[1]}")

    cam = Picamera2()
    preview_config = cam.create_preview_configuration(
        {"format": "BGR888", "size": resolution})
    cam.configure(preview_config)
    cam.start()

    streamer_rgb = VS.VideoStreamer('rgb')
    streamer_rgb.run()

    try:
        while True:
            buffer: npt.NDArray = cam.capture_buffer()
            frame = np.zeros((resolution[1], 2*resolution[0], 3), np.uint8)
            frame[:, :, 2] = np.reshape(
                buffer[0::3], (resolution[1], 2*resolution[0]))
            frame[:, :, 1] = np.reshape(
                buffer[1::3], (resolution[1], 2*resolution[0]))
            frame[:, :, 0] = np.reshape(
                buffer[2::3], (resolution[1], 2*resolution[0]))
            if not right:
                streamer_rgb.publishFrame(frame[:, :resolution[0], :])
            elif not left:
                streamer_rgb.publishFrame(frame[:, resolution[0]+1:, :])
            else:
                streamer_rgb.publishFrame(frame)
    except KeyboardInterrupt:
        print("Finished")
    except Exception as e:
        print(e)
    finally:
        streamer_rgb.close()


if __name__ == "__main__":
    args = sys.argv
    nums = [int(arg) for arg in args if arg.isdecimal()]
    if "-r" in args and "-l" not in args:
        if len(nums) == 2:
            main(nums, 'r')
        else:
            main(camera_choose='r')
    elif "-r" not in args and "-l" in args:
        if len(nums) == 2:
            main(nums, 'l')
        else:
            main(camera_choose='l')
    else:
        if len(nums) == 2:
            main(nums)
        else:
            main()
