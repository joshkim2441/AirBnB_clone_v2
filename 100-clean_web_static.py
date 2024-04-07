#!/usr/bin/python3
""" Deletes out-of-date archives from atatic files """
import os
from fabric.api import *

env.user = 'ubuntu'
env.hosts = ['34.232.53.167', '54.89.195.92']
env.key_filename = "~/id_rsa"

def do_clean(number=0):
    """ Deletes out_of_date archives """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
