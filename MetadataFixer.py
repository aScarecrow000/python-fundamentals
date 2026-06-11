import os
from datetime import datetime
import win32file
import win32con
import pywintypes

def set_creation_time(filepath, timestamp):

    # Open a low-level handle to the file with write permissions
    handle = win32file.CreateFile(
        filepath,
        win32con.GENERIC_WRITE,
        win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE,
        None,
        win32con.OPEN_EXISTING,
        0,
        None
    )

    # Convert our standard timpestamp into a Windows-compatible time format
    #win32_time = win32file.Time(timestamp)
    win32_time = pywintypes.Time(timestamp)

    # Apply it specifically to the file's creation time
    win32file.SetFileTime(handle, win32_time, None, None)

    # safly close the file handle
    handle.close()

print(os.getcwd())
os.chdir('E:\\G\\ME\\ilQar\\Telegram Desktop')
print(os.getcwd())
#print(os.listdir())

# Define the counter for the photos
photo_count = 1

for filename in os.listdir():
    
    if filename.startswith('photo_'):

        # Print the filename being processed with counter
        print(f"{photo_count} Proccessing {filename}...")

        # Filter out the date string from the filename
        date_string = filename[6:25]
        print(f"Date string: {date_string}")
        
        # Convert the date string to a datetime object
        date_object = datetime.strptime(date_string, "%Y-%m-%d_%H-%M-%S")
        print(f"Date object: {date_object}")

        # Convert date object to seconds since epoch
        file_timestamp = int(date_object.timestamp())
        print (f"File timestamp: {file_timestamp}")

        # Update the file's metadata with the new timestamp
        filename = os.path.join(os.getcwd(), filename)
        os.utime(filename, (file_timestamp, file_timestamp))

        # Print a message indicating the file has been updated
        updated_epoch = os.path.getmtime(filename)

        # Convert epoch time back to a human-readable format
        updated_time = datetime.fromtimestamp(updated_epoch).strftime('%Y-%m-%d %H:%M:%S')
        print(f"Updated timestamp for {filename}: {updated_time}\n")

        # Set the creation time using the custom function
        set_creation_time(filename, file_timestamp)

        # Update the counter
        photo_count += 1