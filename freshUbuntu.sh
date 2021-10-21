#! /usr/bin/bash

#Get updates
sudo apt update && sudo apt upgrade -y

#C/C++ compiler
sudo apt install build-essential -y

#MPICH - Message Passing Interface
sudo apt install mpich -y

#Filezilla - SFTP client
sudo apt install filezilla -y

#Yakuake (drop down terminal)
sudo apt install yakuake -y

#Gnome Keyring
sudo apt install gnome-keyring

#Java Development Kit
sudo apt install default-jdk

#Git - Version Control
sudo apt install git

#Configure Git
git config --global user.name "Jon"
git config --global user.email "jon.hogan83@gmail.com"

#Install Snapd
sudo apt install snapd  -y

#install Discord, VS Code, Slack, and Zoom
sudo snap install discord
sudo snap install code --classic
sudo snap install slack --classic
sudo snap install zoom-client
