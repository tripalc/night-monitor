from monitorcontrol import get_monitors
from datetime import datetime
from win10toast import ToastNotifier # Remove this if you aren't on Windows!

levels = {
    0: 5,
    1: 5,
    2: 5,
    3: 5,
    4: 5,
    5: 5,
    6: 20,
    7: 50,
    8: 50,
    9: 50,
    10: 50,
    11: 75,
    12: 75,
    13: 75,
    14: 75,
    15: 75,
    16: 75,
    17: 75,
    18: 75,
    19: 45,
    20: 25,
    21: 15,
    22: 5,
    23: 5,
}

def main(level = 0):
    # If level is not set, set brightness based on time of day
    if level != 0:
        for monitor in get_monitors():
            with monitor:
                monitor.set_luminance(level)

            # Remove this if you aren't on Windows!
            ToastNotifier().show_toast(
                "Brightness adjusted",
                f"Brightness set to {level}%",
                duration=0.01,
                threaded=True,
            )
    
    # Otherwise, set brightness to level requested
    else:
        for monitor in get_monitors():
            with monitor:
                monitor.set_luminance(levels[datetime.now().hour])

            # Remove this if you aren't on Windows!
            ToastNotifier().show_toast(
                "Brightness adjusted",
                f"Brightness set to {levels[datetime.now().hour]}%",
                duration=0.01,
                threaded=True,
            )

if __name__ == "__main__":
    main()