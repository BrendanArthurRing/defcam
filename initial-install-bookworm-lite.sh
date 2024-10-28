#!/bin/bash

# Initial installation for software needed for defcam
sudo apt update 

sudo apt install -y \ 
fbi \ # Software for showing images on the commandline
neofetch \ # useful for checking linux distro info

# to install on raspberry pi os lite with no gui support
sudo apt install -y python3-picamera2 --no-install-recommends

# to prevent RuntimeError: Error waiting for edge when using GPIO.wait_for_edge(4, GPIO.FALLING)
sudo apt remove python3-rpi.gpio
sudo apt install python3-rpi-lgpio
sudo apt autoremove
