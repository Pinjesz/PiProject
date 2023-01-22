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
    i = 0
    try:
        while True:
            time.sleep(0.001)
            if(restAP.isActive()):
                if(restAP.controlChanged()):
                    control = restAP.pollControl()
                    print("Received new control: " + str(control))
                i = perform_control(control, i)

    except KeyboardInterrupt:
        exit()

def perform_control(control:Control, i:int) -> int:
    if Control.is_control_active(control.pan, i):
        if control.pan > 0:
            steering.right()
        else:
            steering.left()
    if Control.is_control_active(control.tilt, i):
        if control.tilt > 0:
            steering.up()
        else:
            steering.down()

    if control.laser:
        steering.laser_on()
    else:
        steering.laser_off()

    return (i+1) % 10

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
