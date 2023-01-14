from RestAPI.server import restAP
import time
import threading
import CameraRead
import sys


def run(resolution: list = (640, 480), camera_choose: str = 'b'):
    # Start server as daemon:
    restAP.run_async()

    print("Server started on address localhost:5000/api")
    print("Documentation accessible at http://localhost:5000/api/doc")

    def run_camera():
        CameraRead.run(resolution, camera_choose)

    cameras = threading.Thread(target=run_camera)
    cameras.daemon = True
    cameras.start()

    while True:
        try:
            time.sleep(0.001)
            if(restAP.controlChanged()):
                control = restAP.pollControl()
                print("Received new control: " + str(control))

        except KeyboardInterrupt:
            break

    cameras.join()
    restAP.stop_async()


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
