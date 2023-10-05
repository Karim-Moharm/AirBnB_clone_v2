#!/usr/bin/env bash
# prepare the web server

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

