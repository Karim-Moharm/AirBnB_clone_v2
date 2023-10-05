#!/usr/bin/env bash
# Prepare the web servers 

sudo apt update
sudo apt install nginx -y
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

sudo echo "
        <html>
          <head>
            <title>Test</title>
          </head>
          <body>
            Hello friend
          </body>
        </html>
" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data

# modify default file
CONFIG_PATH="/etc/nginx/sites-available/default"
# CONFIG_PART="\tlocation /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}\n"

:<<COMMENT
LOCATION_BLOCK="\
        location /hbnb_static/ {\
                alias /data/web_static/current/;\
    }"
COMMENT

# write at line 25 inside the server block
sudo sed -i "25i \\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" "$CONFIG_PATH"

# sudo echo "$LOCATION_BLOCK" | sudo tee -a "$CONFIG_PATH"

sudo service nginx restart
