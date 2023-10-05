
eudo service nginx restart
sre the web server

sudo apt update
sudo apt install nginx -y
sudo mkdir -p /data/web_static/{releases/test,shared}

sudo echo "
        <html>
          <head>
            <title>Test</title>
          </head>
          <body>
            Hello friend
          </body>
        </html>
" | sudo tee -a /data/web_static/releases/test/index.html

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
sudo sed -i "25i \\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default

sudo echo "$LOCATION_BLOCK" | sudo tee -a "$CONFIG_PATH"

sudo service nginx restart
udo service nginx restart
