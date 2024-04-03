#!/usr/bin/env bash
# script that sets up web servers for the deployment of web_static

# Update package lists
sudo apt-get update

# Install Nginx
sudo apt-get -y install nginx

# Allow incoming HTTP traffic through the firewall
sudo ufw allow 'Nginx HTTP'

# Create necessary directories
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Create an empty index.html file
sudo touch /data/web_static/releases/test/index.html

# Add content to the index.html file
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link to the current release
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

# Change ownership of the directories to 'ubuntu' user and group
sudo chown -R ubuntu:ubuntu /data/

# Configure Nginx to serve the static files
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# Restart Nginx to apply the configuration changes
sudo service nginx restart
