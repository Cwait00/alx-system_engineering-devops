#!/usr/bin/env bash
# This script configures Nginx to listen on port 80 and serve a specific domain or IP.

# Replace 'yourdomain.com' with the actual domain or IP address
DOMAIN_OR_IP="192.124.249.6"

# Install Nginx if not already installed
sudo apt-get update
sudo apt-get install -y nginx

# Remove default Nginx configuration
sudo rm -f /etc/nginx/sites-available/default
sudo rm -f /etc/nginx/sites-enabled/default

# Create and configure a new Nginx site
sudo tee /etc/nginx/sites-available/web-01 > /dev/null <<EOL
server {
    listen 80;
    listen [::]:80;

    server_name $DOMAIN_OR_IP;

    location /hbnb_static {
        alias /data/web_static/current/;
    }

    add_header X-Served-By \$hostname;

    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
    }
}
EOL

# Create a symbolic link to enable the site
sudo ln -s /etc/nginx/sites-available/web-01 /etc/nginx/sites-enabled/

# Test Nginx configuration
sudo nginx -t

# Restart Nginx to apply changes
sudo service nginx restart
