#!/usr/bin/python3
"""
Fabric script based on the file 2-do_deploy_web_static.py that creates and
distributes an archive to the web servers
"""

from fabric.api import *
from fabric.operations import run, put, sudo, local
from datetime import datetime
import os

env.hosts = ['34.232.53.167', '54.89.195.92']
created_path = None


@runs_once
def do_pack():
    """ Generates a .tgz archive from contents
    of the web_static folder
    """
    tm = datetime.now()
    tm_ft = tm.strftime("%Y%m%d%H%M%S")
    if not os.path.isdir("versions"):
        local("mkdir versions")
    file_path = "versions/web_static_{}.tgz".format(tm_ft)
    result = local("tar -cvzf {} web_static".format(file_path))
    if result.failed:
        return None
    archize_size = os.stat(file_path).st_size
    print("web_static packed: {} -> {} Bytes".format(file_path, archize_size))
    return file_path


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if os.path.exists(archive_path) is False:
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
    except Exception:
        return False


def deploy():
    """
        deploy function that creates/distributes an archive
    """
    global created_path
    if created_path is None:
        created_path = do_pack()
    if created_path is None:
        return False
    return do_deploy(created_path)
