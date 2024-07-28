
```markdown
# USB Sentinel

USB Sentinel is a Python project that monitors USB device activity and logs suspicious activity on the connected USB devices. It provides real-time alerts for USB device insertion, removal, and file modifications.

## Prerequisites

Before running the USB Sentinel project, make sure you have the following prerequisites installed:

- Python 3.x
- pip

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/sathvik-shettyy/usb-sentinel.git
   ```

2. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

## Configuration

The USB Sentinel project uses a configuration file (`config.ini`) to specify the logging level, log file name, monitoring path, and suspicious activity check interval. You can customize these settings according to your needs.

- **Logging**: The `config.ini` file allows you to specify the logging level and log file name. The logging level can be set to `INFO`, `DEBUG`, `ERROR`, etc. The log file name can be modified to specify the desired log file location.

- **Monitoring**: The `config.ini` file allows you to specify the path to the USB device or directory you want to monitor. By default, the monitoring path is set to `./Logs-Alerts.log-file_activity.log`.

- **Suspicious Activity**: The `config.ini` file allows you to specify the interval (in seconds) at which the system should check for suspicious activity. By default, the check interval is set to 60 seconds.

## Usage

To start the USB Sentinel project, run the following command:

```shell
python usb_sentinel.py
```

The project will start monitoring the USB device activity and log any suspicious activity in the specified log files.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

Feel free to customize the `README.md` file according to your project's specific details and requirements.

