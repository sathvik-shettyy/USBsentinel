import logging
import os
import pyusb
import time
import watchdog.events
import watchdog.observers

def monitor_usb_devices():
    previous_devices = set()

    while True:
        current_devices = set(pyusb.core.find(find_all=True))

        added_devices = current_devices - previous_devices
        removed_devices = previous_devices - current_devices

        for device in added_devices:
            logging.info(f"USB device inserted: {device}")

        for device in removed_devices:
            logging.info(f"USB device removed: {device}")

        previous_devices = current_devices

def start_file_monitoring(usb_device_path):
    event_handler = watchdog.events.FileSystemEventHandler()

    @event_handler.on_any_event
    def on_event(event):
        if event.is_directory:
            return

        logging.info(f"USB device file modified: {event.src_path}")

    observer = watchdog.observers.Observer()
    observer.schedule(event_handler, usb_device_path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

def detect_suspicious_activity():
    previous_access_times = {}
    previous_modification_times = {}

    while True:
        try:
            usb_device_path = "/path/to/usb_device"
            files = os.listdir(usb_device_path)

            for file_name in files:
                file_path = os.path.join(usb_device_path, file_name)
                current_access_time = os.stat(file_path).st_atime
                current_modification_time = os.stat(file_path).st_mtime

                if file_name not in previous_access_times or current_access_time != previous_access_times[file_name]:
                    logging.warning(f"Suspicious access detected on file {file_name}: {file_path}")
                    previous_access_times[file_name] = current_access_time

                if file_name not in previous_modification_times or current_modification_time != previous_modification_times[file_name]:
                    logging.warning(f"Suspicious modification detected on file {file_name}: {file_path}")
                    previous_modification_times[file_name] = current_modification_time
        except Exception as e:
            logging.error(f"Error detecting suspicious activity: {str(e)}")

            time.sleep(1)

if __name__ == "__main__":
    monitor_usb_devices()
    start_file_monitoring("./Logs-Alerts.log-file_activity.log")
    detect_suspicious_activity()