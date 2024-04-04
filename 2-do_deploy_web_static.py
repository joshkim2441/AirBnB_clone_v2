#!/usr/bin/python3
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['34.232.53.167', '54.89.195.92']


def do_deploy(archive_path):
    """ Distributes an archive to web servers. """
    if exists(archive_path):
        try:
            # Upload the archive to the /tmp/ directory
            # of the web server

            # Uncompress the archive to the folder /dat/web_static
            # /releases/ on the web sserver
            file_name = archive_path.split("/")[-1]
            name = file_name.split(".")[0]
            path = "/data/web_static/releases/"
            put(archive_path, "/tmp/{}".format(file_name))
            run("mkdir -p {}/".format(path, name))
            run("tar -xzf /tmp/{} -C {}/".format(file_name, path, name))
            # Delete the archive from the web server
            run("rm /tmp/{}".format(file_name))
            run("mv {}/web_static/* {}/".format(path, name, path, name))
            run("rm -rf {}/web_static".format(path, name))
            # Delete the symbolic link /data/web_static/current from web server
            run("rm -rf /data/web_static/current")
            # Create a new symbolic link /data/web_static/current on web server
            run("ln -s {}/ /data/web_static/current".format(path, name))
            print("New version deployed!")
            return True
        except Exception:
            return False
    return False
