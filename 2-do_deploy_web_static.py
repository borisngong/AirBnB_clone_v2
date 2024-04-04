#!/usr/bin/python3
"""
A Fabric script based on 1-pack_web_static.py that distributes an
archive to your web servers, using the function do_deploy
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['18.234.192.1', '54.160.85.43']


def do_deploy(archive_path):
    """
    Distribute an archive to the web servers by performing these steps:
    -Check if the archive file exists.
    -Upload the archive to the remote servers.
    -Extract the contents of the archive to the appropriate directory
     on each server.
    -Remove the temporary archive file.
    -Move the extracted contents to the correct location.
    -Remove the original web_static directory.
    -Create a symbolic link from /data/web_static/current to the new
     deployment.
    Args:
        archive_path (str): The local path to the archive file to be
        distributed.
    Returns:
        bool: True if the deployment is successful, False otherwise.
    """
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False
