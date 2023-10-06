#!/usr/bin/python3
"""script used to Deploy archive
"""
import os
from fabric.api import local, put, run, env 

env.hosts = ['100.25.23.34', '52.87.216.135']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """script that distributes an archive to your web servers,
    using the function do_deploy
    """
    if not os.path.exists(archive_path):
        return False

    # versions/file.tgz
    file_name_without_ext = archive_path.split('/')[-1].split('.')[0]
    file_name_with_ext = archive_path.split('/')[-1]
    uncompress_path = '/data/web_static/releases/{}'\
                      .format(file_name_without_ext)

    put(archive_path, '/tmp/')
    result = run('mkdir -p {}'.format(uncompress_path))
    if result.failed:
        return False

    result = run('tar -xzf /tmp/{} -C {}'.format(
                  file_name_with_ext, uncompress_path))
    if result.failed:
        return False

    result = run('rm /tmp/{}'.format(file_name_with_ext))
    if result.failed:
        return False

    result = run('mv {}/web_static/* {}/'.format(
                 uncompress_path, uncompress_path))
    if result.failed:
        return False

    result = run('rm -rf {}/web_static'.format(uncompress_path))
    if result.failed:
        return False

    result = run('rm -rf /data/web_static/current')
    if result.failed:
        return False

    result = run('ln -sf {} /data/web_static/current'.format(uncompress_path))
    if result.failed:
        return False
    print("New version deployed!")
    return True
