#!/bin/bash
echo "UBUNTU POST-INSTALL SCRIPT"
echo "Updating APT..."
sudo apt-get update
echo "Installing base packages"
sudo apt-get install --yes git git-extras build-essential python3-pip htop glances
echo "Installing Visual Studio code"
sudo sudo snap install code 
echo "Installing Discord"
sudo sudo snap install discord
clear 

