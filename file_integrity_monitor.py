import os
import hashlib
import time
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email):
    """Send an email notification using Yahoo Mail's SMTP server."""
    from_email = "your_email@yahoo.com"
    password = "your_app_password"  # Use your Yahoo app password here if 2-Step Verification is enabled

    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = subject
    
    message.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, message.as_string())
        server.quit()
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

def calculate_hash(file_path):
    """Calculate SHA-256 hash of the file."""
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

def normalize_path(file_path):
    """Normalize the file path for consistent comparison."""
    return os.path.abspath(file_path)

def monitor_directory(directory, baseline_file, notified_file, interval=30):
    """Monitor directory for file changes."""
    if os.path.exists(baseline_file):
        with open(baseline_file, "r") as f:
            baseline_hashes = json.load(f)
    else:
        baseline_hashes = {}

    if os.path.exists(notified_file):
        with open(notified_file, "r") as f:
            notified_changes = json.load(f)
    else:
        notified_changes = {}

    try:
        while True:
            current_hashes = {}
            modified_files = []

            for root, _, files in os.walk(directory):
                for file in files:
                    file_path = normalize_path(os.path.join(root, file))
                    current_hash = calculate_hash(file_path)
                    current_hashes[file_path] = current_hash

                    if file_path not in baseline_hashes:
                        print(f"New file detected: {file_path}")
                        if file_path not in notified_changes:
                            modified_files.append(f"New file detected: {file_path}")
                            notified_changes[file_path] = current_hash
                    elif baseline_hashes[file_path] != current_hash:
                        print(f"File modified: {file_path}")
                        if file_path not in notified_changes or notified_changes[file_path] != current_hash:
                            modified_files.append(f"File modified: {file_path}")
                            notified_changes[file_path] = current_hash

            # Save the current state as the new baseline
            with open(baseline_file, "w") as f:
                json.dump(current_hashes, f, indent=4)

            # Save the notified changes to avoid repeated notifications
            with open(notified_file, "w") as f:
                json.dump(notified_changes, f, indent=4)

            if modified_files:
                body = "\n".join(modified_files)
                send_email("File Integrity Monitor Alert", body, "recipient_email@example.com")
                print(f"Detected changes in {len(modified_files)} files.")
            else:
                print("No changes detected.")

            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nMonitoring stopped. Exiting program...")

if __name__ == "__main__":
    directory_to_monitor = r"C:\Users\UserName\Downloads"  # Replace with your directory
    baseline_file = "file_hashes.json"
    notified_file = "notified_changes.json"
    monitor_interval = 30  # Check every 30 seconds

    monitor_directory(directory_to_monitor, baseline_file, notified_file, monitor_interval)
