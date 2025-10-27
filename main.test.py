from monitorcontrol import get_monitors
from datetime import datetime
from win11toast import notify
from json import load
from pathlib import Path

def main():
    date_and_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log(f"=== {date_and_time} ===")
    set_brightness()

def log(message):
    with open("log", "a") as log:
        log.write(f"{message}\n")

def end(code):
    log(f"[INFO] Exiting with code {code}.")
    exit(code)

def load_options() -> dict:
    options_location = Path("options.json")

    if options_location.is_file():
        with open("options.json", "r") as file:
            options = load(file)
            log("[OK] Options file loaded.")
            return options

    else:
        notify(title="Night Monitor", body="No options found. Please set options.json file!")
        log("[ERROR] Options not found. Please set options.json file!")
        end(1)

def set_brightness():
    options = load_options()
    levels = options["levels"]
    notification = options["notification"]

    hour = datetime.now().hour

    for monitor in get_monitors():
        with monitor:
            monitor.set_luminance(levels[hour])

    log(f"[OK] Brightness set to {levels[hour]}%.")

    if notification:
        notify(title="Night Monitor", body=f"Brightness set to {levels[hour]}%")
        log("[INFO] Sent out notification.")

if __name__ == "__main__":
    main()
    end(0)