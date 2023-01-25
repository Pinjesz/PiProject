import RTMPVideo.streaming.VideoStreamer as VS
import numpy.typing as npt
import numpy as np
import sys
from picamera2 import Picamera2


def run(resolution: list = (640, 480), camera_choose: str = 'b'):
    left = True
    right = True
    width = resolution[0]
    height = resolution[1]
    if camera_choose == 'l':
        right = False
        print(f"Left camera, resolution: {resolution[0]} x {resolution[1]}")
    elif camera_choose == 'r':
        left = False
        print(f"Right camera, resolution: {resolution[0]} x {resolution[1]}")
    else:
        print(f"Both cameras, resolution: {resolution[0]} x {resolution[1]}")
        width = 2*width

    cam = Picamera2()
    preview_config = cam.create_preview_configuration(
        {"format": "RGB888", "size": (2*resolution[0], resolution[1])})
    cam.configure(preview_config)
    cam.start()

    streamer_rgb = VS.VideoStreamer('rgb', width=width, height=height)
    streamer_rgb.run()

    try:
        while True:
            try:
                buffer: npt.NDArray = cam.capture_buffer()
            except Exception as e:
                print("Error getting buffer: ", e)
            frame = np.zeros((resolution[1], 2*resolution[0], 3), np.uint8)
            frame[:, :, 0] = np.reshape(    # R
                buffer[0::3], (resolution[1], 2*resolution[0]))
            frame[:, :, 1] = np.reshape(    # G
                buffer[1::3], (resolution[1], 2*resolution[0]))
            frame[:, :, 2] = np.reshape(    # B
                buffer[2::3], (resolution[1], 2*resolution[0]))
            try:
                if not right:
                    streamer_rgb.publishFrame(frame[:, :resolution[0], :])
                elif not left:
                    streamer_rgb.publishFrame(frame[:, resolution[0]+1:, :])
                else:
                    streamer_rgb.publishFrame(frame)
            except Exception as e:
                print("Error sending frame: ", e)
    except KeyboardInterrupt:
        print("Finished")
    except Exception as e:
        print("Something is wrong:", e)
    finally:
        streamer_rgb.close()


if __name__ == "__main__":
    args = sys.argv
    nums = [int(arg) for arg in args if arg.isdecimal()]
    if "-r" in args and "-l" not in args:
        if len(nums) == 2:
            run(nums, 'r')
        else:
            run(camera_choose='r')
    elif "-r" not in args and "-l" in args:
        if len(nums) == 2:
            run(nums, 'l')
        else:
            run(camera_choose='l')
    else:
        if len(nums) == 2:
            run(nums)
        else:
            run()
