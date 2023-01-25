from RestAPI.server import restAP
import time
import threading
import CameraRead
import sys
import steering
from RestAPI.synchronized.SControl import Control


def run(resolution: list = (640, 480), camera_choose: str = 'b'):
    # Start server as daemon:
    restAP.run_async()

    print("Server started on address localhost:5000/api")
    print("Documentation accessible at http://localhost:5000/api/doc")

    def run_camera():
        CameraRead.run(resolution, camera_choose)

    cameras_thread = threading.Thread(target=run_camera)
    cameras_thread.daemon = True
    cameras_thread.start()

    steering.setup_pins()
    control = Control()
    try:
        while True:
            time.sleep(0.001)
            if(restAP.isActive()):
                if(restAP.controlChanged()):
                    control = restAP.pollControl()
                    print("Received new control: " + str(control))

                control = perform_control(control)

    except KeyboardInterrupt:
        exit()


def perform_control(control: Control) -> Control:
    if control.laser:
        steering.laser_on()
    else:
        steering.laser_off()

    pan_diff = control.set_pan-control.current_pan
    pan_angle = 0
    if pan_diff <= -1:
        steering.left()
        pan_angle = -0.3
    if pan_diff >= 1:
        steering.right()
        pan_angle = 0.3

    tilt_diff = control.set_tilt-control.current_tilt
    tilt_angle = 0
    if tilt_diff <= -1:
        steering.down()
        tilt_angle = -1
    if tilt_diff >= 1:
        steering.up()
        tilt_angle = 1

    restAP.updateControl(pan_angle, tilt_angle)
    return restAP.lookupControl()


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
