#!/usr/bin/python3
"""script used to Deploy archive
"""
import os
from fabric.api import local, run, get, env
from datetime import datetime

env.hosts = ['100.25.23.34', '52.87.216.135']
env.user = 'ubuntu'


def do_pack():
    """generates a .tgz archive from the contents of the web_static folder
    """
    formatted_dt = datetime.now().strftime("%Y%m%d%H%M%S")
    archieve_name = "web_static_{}.tgz".format(formatted_dt)

    try:
        local("mkdir -p versions")
        result = local("tar -czvf versions/{} versions".format(archieve_name))
        file_size = os.path.getsize("versions/{}".format(archieve_name))
        print("web_static packed: versions/{} -> {}Bytes".format(archieve_name,
                                                                 file_size))
        if result.succeeded:
            return f"versions/{archieve_name}"
        else:
            return None
    except Exception:
        return None


def do_deploy(archive_path):
    """script that distributes an archive to your web servers,
    using the function do_deploy
    """
    if not os.path.exists(archive_path):
        return False

    # versions/file.tgz
    try:
        file_name_without_ext = archive_path.split('/')[-1].split('.')[0]
        file_name_with_ext = archive_path.split('/')[-1]
        uncompress_path = '/data/web_static/releases/{}'\
                          .format(file_name_without_ext)

        put(archive_path, '/tmp/')
        run('mkdir -p {}'.format(uncompress_path))
        run('tar -xvzf /tmp/{} -C {}'.format(
            file_name_with_ext, uncompress_path))
        run('rm /tmp/{}'.format(file_name_with_ext))
        run('mv {}/web_static/* {}/'.format(uncompress_path, uncompress_path))
        run('rm -rf {}/web_static'.format(uncompress_path))

        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(uncompress_path))
        return True
    except Exception:
        return False
