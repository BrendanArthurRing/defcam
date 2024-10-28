import picamera2
import time
import RPi.GPIO as GPIO

# Set up GPIO for button 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initialize the camera
picam2 = picamera2.Picamera2()

# Edit controls
picam2.camera_controls["Saturation"] = 0


camera_config = picam2.create_still_configuration()


# Modify the camera configuration
#camera_config["Saturation"] = 0.0  # Increase saturation (values > 1.0)
# Other controls you can adjust:
# camera_config["Sharpness"] = 1.5  # Increase sharpness
# camera_config["Contrast"] = 1.2  # Increase contrast
# camera_config["Brightness"] = 0.1  # Increase brightness (0.0 to 1.0)
# ... and many more!


# Configure the camera with the modified configuration
picam2.configure(camera_config)
picam2.start()

def capture_image():
    # Generate a filename based on the current timestamp
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"image_{timestamp}.jpg"
    
    # Capture the image
    picam2.capture_file(filename)
    print(f"Image captured and saved as {filename}")

try:
    while True:
        # Wait for button press
        GPIO.wait_for_edge(4, GPIO.FALLING)
        
        # Debounce the button (optional, but recommended)
        time.sleep(0.2)
        
        # Capture the image
        capture_image()

finally:
    # Clean up GPIO on exit
    GPIO.cleanup()
    picam2.stop()
