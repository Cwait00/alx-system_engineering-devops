echo "[STUDENT_ID]-web-01" | sudo tee /etc/hostname
sudo sed -i '/127.0.0.1/s/$/ [STUDENT_ID]-web-01/' /etc/hosts
sudo hostnamectl set-hostname [STUDENT_ID]-web-01
