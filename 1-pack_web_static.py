#!/usr/bin/env bash
# Generates a .tgz archive from the contents of web_static
# folder of AirBnB Clone repo using the function do_pack

import os
from fabric.api import *
from datetime import datetime


def do_pack():
    """ Generates a .tgz archive from contents
    of the web_static folder
    """
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    if os.path.isdir("versions") is False:
        local("mkdir versions")
    file_path = "versions/web_static_{}{}{}{}{}{}.tgz".format(time)
    archize_size = os.stat(time).st_size
    result = local("tar -cvzf {} web_static".format(file_path))
    print("web_static packed: {} -> {} Bytes".format(file_path, archize_size))
    if result.failed:
        return None
    return file_path
