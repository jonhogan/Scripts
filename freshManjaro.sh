#! /usr/bin/bash

#Get updates
sudo pacman -Syu -y

#Install C/C++ compiler
sudo pacman -Sy base-devel -y

#Install and set up Snapd
sudo pacman -S snapd -y
sudo systemctl enable --now snapd.socket

sudo ln -s /var/lib/snapd/snap /snap -y

#install VS Code, Discord, Slack, and Zoom
sudo snap install code --classic
sudo snap install Discord
sudo snap install slack --classic
sudo snap install zoom-client

#install Java
#sudo pacman -S jdk-openjdk openjdk-src -y

#install Filezilla
#sudo pamac install filezilla -y
