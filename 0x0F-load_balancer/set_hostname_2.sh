#!/usr/bin/env bash

# Set the hostname for [STUDENT_ID]-web-02
echo "[STUDENT_ID]-web-02" | sudo tee /etc/hostname

# Add the hostname to /etc/hosts
sudo sed -i '/127.0.0.1/s/$/ [STUDENT_ID]-web-02/' /etc/hosts

# Set the hostname using hostnamectl
sudo hostnamectl set-hostname [STUDENT_ID]-web-02
