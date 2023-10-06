#!/usr/bin/python3
"""script used to Deploy archive
"""
import os
from fabric.api import local, run, get, env

env.hosts = ['100.25.23.34', '52.87.216.135']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """script that distributes an archive to your web servers,
    using the function do_deploy
    """ 
    # versions/file.tgz
    file_name_without_ext = archive_path.split('/')[1].split('.')[0]
    file_name_with_ext = archive_path.split('/')[1]
    uncompress_path = '/data/web_static/releases/{}'\
                      .format(file_name_without_ext)

    if os.path.exists(archive_path):
        put(archive_path, '/tmp/')
        run('tar -xvzf /tmp/{} -C {}'.format(
            file_name_with_ext, uncompress_path))
        run('rm /tmp/{}'.format(file_name_with_ext))
        run('mv {}/web_static/* {}/'.format(uncompress_path, uncompress_path))
        run('rm -rf {}/web_static'.format(uncompress_path))

        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(uncompress_path))
        return True
    return False
