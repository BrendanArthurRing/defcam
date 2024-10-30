#!/bin/bash

# Initial installation for software needed for defcam
sudo apt update 

sudo apt install -y \ 
fbi \ # Software for showing images on the commandline
neofetch \ # useful for checking linux distro info
i2c-tools # needed for using pisugar

# to install on raspberry pi os lite with no gui support
sudo apt install -y python3-picamera2 --no-install-recommends

# to prevent RuntimeError: Error waiting for edge when using GPIO.wait_for_edge(4, GPIO.FALLING)
sudo apt remove python3-rpi.gpio
sudo apt install python3-rpi-lgpio
sudo apt autoremove

# Get current state of i2c, should be off (set to 1) by default at install
#sudo raspi-config nonint get_i2c

# Enable i2c
sudo raspi-config nonint do_i2c 0

# detect i2c bus and devices
i2cdetect -y 1
i2cdump -y 1 0x32
i2cdump -y 1 0x75

wget https://cdn.pisugar.com/release/pisugar-power-manager.sh
bash pisugar-power-manager.sh -c release

echo 'lpf () {latest_photo=$(find /home/$USER/photos/ -name "*.jpg" -printf "%T@ %p\n" | sort -nr | head -1 | awk \'{print $2}\') ; fbi -a "$latest_photo" ; }' >> /home/$USER/.bashrc
source /home/$USER/.bashrc

