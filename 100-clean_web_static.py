#!/usr/bin/python3
""" Deletes out-of-date archives from atatic files """
import os
from fabric.api import *

env.user = 'ubuntu'
env.hosts = ['34.232.53.167', '54.89.195.92']
env.key_filename = "~/id_rsa"

def do_clean(number=0):
    """ Deletes out_of_date archives """
    try:
        number = int(number)
    except ValueError:
        print("The 'number' parameter must be an integer.")
        return False

    number = max(1, number)

    try:
        archives = sorted(os.listdir("versions"))
    except FileNotFoundError:
        print("The 'versions' directory does not exist.")
        return False

    [archives.pop() for _ in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for _ in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]

    return True
