
# Import AccessPoint variable form server package:
from MPcomms.RestAPI.server import restAP

# Other imports:
import time

if __name__ == "__main__":
    # Start server as daemon:
    restAP.run_async()

    print("Server started on address localhost:5000/api")
    print("Documentation accessible at http://localhost:5000/api/doc")

    while True:
        try:
            time.sleep(0.001)
            if(restAP.controlChanged()):
                control = restAP.pollControl()
                print("Received new control: " + str(control))
        except KeyboardInterrupt:
            break
