# File Integrity Monitor

## Overview
The File Integrity Monitor is a Python script that monitors files in a specified directory for changes, such as modifications, additions, or deletions. It calculates and compares the SHA-256 hash values of the files to detect any alterations. When a change is detected, the script alerts the user by printing a message to the console.

## Features
- **Hash-based Monitoring:** Uses SHA-256 to detect file modifications.
- **Real-time Monitoring:** Periodically checks the directory for changes. (60 Seconds by default).
- **Detection of New Files:** Alerts the user when new files are added to the directory.
- **Detection of Modified Files:** Alerts the user when existing files are modified.
- **Cross-Platform Support:** Compatible with both Windows and Unix-based systems.

### Usage and Customization
- Open the script file_integrity_monitor.py and set the directory_to_monitor variable to the path of the directory you want to monitor.
- -You can change the monitoring interval by modifying the monitor_interval variable in seconds:


### Prerequisites
- Python 3.x

###
- Created with help from LLM.

### Clone the Repository
```bash
git clone https://github.com/yourusername/file-integrity-monitor.git
cd file-integrity-monitor
