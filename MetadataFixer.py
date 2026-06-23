import os
import sys
from datetime import datetime
import argparse

# 1. Safe Cross-Platform Imports
if sys.platform == "win32":
    import win32file
    import win32con
    import pywintypes
else:
    win32file = None
    win32con = None
    pywintypes = None

# 2. Optimized Argparse Configuration
default_folder = os.getcwd()
help_text = f"Path to the folder containing the photos. Default is current working directory: {default_folder}"

arg_parser = argparse.ArgumentParser(
    description="Fix photo metadata based on filename."
)
arg_parser.add_argument(
    "-f", "--folder", type=str, default=default_folder, help=help_text
)
args = arg_parser.parse_args()

target_folder = args.folder


def set_creation_time(filepath, timestamp):
    # Open a low-level handle to the file with write permissions
    handle = win32file.CreateFile(
        filepath,
        win32con.GENERIC_WRITE,
        win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE,
        None,
        win32con.OPEN_EXISTING,
        0,
        None,
    )

    # Convert our standard timestamp into a Windows-compatible time format
    win32_time = pywintypes.Time(timestamp)

    # Apply it specifically to the file's creation time
    win32file.SetFileTime(handle, win32_time, None, None)

    # Safely close the file handle
    handle.close()


# Define the counter for the photos
photo_count = 1

print(f"Scanning target folder: {target_folder}\n")

for filename in os.listdir(target_folder):
    if filename.startswith("photo_"):
        print(f"{photo_count} Processing {filename}...")

        # Filter out the date string from the filename
        date_string = filename[6:25]
        print(f"  Date string: {date_string}")

        # Convert the date string to a datetime object
        date_object = datetime.strptime(date_string, "%Y-%m-%d_%H-%M-%S")
        print(f"  Date object: {date_object}")

        # Convert date object to seconds since epoch
        file_timestamp = int(date_object.timestamp())
        print(f"  File timestamp: {file_timestamp}")

        # 3. Create a dedicated full_path variable instead of overwriting 'filename'
        full_path = os.path.join(target_folder, filename)
        os.utime(full_path, (file_timestamp, file_timestamp))

        # Print a message indicating the file has been updated
        updated_epoch = os.path.getmtime(full_path)
        updated_time = datetime.fromtimestamp(updated_epoch).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        print(f"  Updated modification timestamp: {updated_time}")

        # Apply Windows creation time modification conditionally
        if sys.platform == "win32":
            set_creation_time(full_path, file_timestamp)
            print("  Updated creation timestamp successfully.")
        else:
            print("  Skipped Windows creation time update (Unsupported on this OS).")

        print("-" * 40)
        photo_count += 1
