#!/usr/bin/env python3
# Generates a .tgz archive from the contents of web_static
# folder of AirBnB Clone repo using the function do_pack

import os
from fabric.api import *
from datetime import datetime


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
