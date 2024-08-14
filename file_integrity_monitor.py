import os
import hashlib
import time
import json

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

def monitor_directory(directory, baseline_file, interval=60):
    """Monitor directory for file changes."""
    if os.path.exists(baseline_file):
        with open(baseline_file, "r") as f:
            baseline_hashes = json.load(f)
    else:
        baseline_hashes = {}

    try:
        while True:
            current_hashes = {}
            modified_files = []

            for root, _, files in os.walk(directory):
                for file in files:
                    file_path = normalize_path(os.path.join(root, file))
                    current_hash = calculate_hash(file_path)
                    current_hashes[file_path] = current_hash

                    # Check if the file is new or has been modified
                    if file_path not in baseline_hashes:
                        print(f"New file detected: {file_path}")
                    elif baseline_hashes[file_path] != current_hash:
                        print(f"File modified: {file_path}")
                        modified_files.append(file_path)

            # Save the current state as the new baseline
            with open(baseline_file, "w") as f:
                json.dump(current_hashes, f, indent=4)

            if modified_files:
                print(f"Detected changes in {len(modified_files)} files.")
            else:
                print("No changes detected.")

            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nMonitoring stopped. Exiting program...")

if __name__ == "__main__":
    directory_to_monitor = r"C:\Users\JoeSchmo\Downloads"  # Replace with your directory
    baseline_file = "file_hashes.json"
    monitor_interval = 60  # Check every 60 seconds

    monitor_directory(directory_to_monitor, baseline_file, monitor_interval)
