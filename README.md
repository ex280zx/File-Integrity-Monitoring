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
- This uses yahoo SMTP as the sending email source. (See Yahoo SMTP description)
- Open the script file_integrity_monitor.py and set the directory_to_monitor variable to the path of the directory you want to monitor.
- You can change the monitoring interval by modifying the monitor_interval variable in seconds. Default is 30 seconds.

### Yahoo SMTP Explanation:
Yahoo is used since Google recently moved to OAuth.
App Password: If you're using 2-Step Verification, you'll need to generate an app password in your Yahoo account settings and use it in the script instead of your regular Yahoo account password.


### Creation note
- Created with help from LLM.

### Prerequisites
- Python 3.x

### Clone the Repository
```bash
git clone https://github.com/yourusername/file-integrity-monitor.git
cd file-integrity-monitor
