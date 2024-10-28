#!/bin/bash

# Initial installation for software needed for defcam
sudo apt update 

sudo apt install -y \ 
fbi \ # Software for showing images on the commandline
neofetch \ # useful for checking linux distro info

# to install on os
sudo apt install -y python3-picamera2 

# for using gui
sudo apt install -y python3-pyqt5 python3-opengl
