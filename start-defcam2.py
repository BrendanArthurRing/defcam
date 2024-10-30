import os
import picamera2
import time
import RPi.GPIO as GPIO
from datetime import datetime

# Set up GPIO for button 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initialize the camera
picam2 = picamera2.Picamera2()

camera_config = picam2.create_still_configuration(
    controls={
        "Saturation": 0.0,  # Floating point number from 0.0 to 32.0
        "Sharpness": 5.0,  # Floating point number from 0.0 to 16.0
        #"Contrast": 0.0,  # Floating point number from 0.0 to 32.0
        "AwbEnable": False,  # Turn on or off with True False
    }
)

print("Camera Configuration")
print(camera_config)

# Configure the camera with the modified configuration
picam2.configure(camera_config)
picam2.start()

def create_folder():
    # Get the current date in YYYY-MM-DD format
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    # Construct the path to the folder
    folder_path = os.path.join("/home", os.getlogin(), current_date)
    
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    return folder_path

def capture_image(folder_path):
    # Generate a filename based on the current timestamp
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"image_{timestamp}.jpg"
    
    # Construct the full path to the image file
    file_path = os.path.join(folder_path, filename)
    
    # Capture the image
    picam2.capture_file(file_path)
    print(f"Image captured and saved as {filename}")

try:
    # Create the folder for today's images
    folder_path = create_folder()

    while True:
        # Wait for button press
        GPIO.wait_for_edge(4, GPIO.FALLING)
        
        # Debounce the button (optional, but recommended)
        time.sleep(0.2)
        
        # Capture the image
        capture_image(folder_path)

finally:
    # Clean up GPIO on exit
    GPIO.cleanup()
    picam2.stop()
