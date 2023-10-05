#!/usr/bin/python3
"""module to compress file
"""
from fabric.api import local, run
from datetime import datetime
import os

def do_pack():
	"""generates a .tgz archive from the contents of the web_static folder
	"""
	formatted_dt = datetime.now().strftime("%Y%m%d%H%M%S")
	archieve_name = "web_static_{}.tgz".format(formatted_dt)

	try:
		local("mkdir -p versions")
		local("tar -czvf versions/{} versions".format(archieve_name))
		file_size = os.path.getsize("versions/{}".format(archieve_name))
		print("web_static packed: versions/{} -> {}Bytes".format(archieve_name, file_size))		
	except:
		return None
		
	
