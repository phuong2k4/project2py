import time

from jedi.inference.gradual.generics import TupleGenericManager
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title= "Alert",
            message = "This alert from python package!",
            timeout = 10
        )
        time.sleep(1600)

