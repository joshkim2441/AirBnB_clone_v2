#!/usr/bin/python3
from fabric.api import *
from datetime import datetime
import os

env.hosts = ['34.232.53.167', '54.89.195.92']


def do_clean(number=0):
    """ Deletes out_of_date archives """
    number = int(number)
    if number < 2:
        number = 1
    else:
        number += 1

    paths = ["versions/*", "/data/web_static/releases/*"]
    for path in paths:
        cmd = ("ls -dt {} | tail -n {} | xargs rm -rf".
        format(path, number))
    local(cmd) if path == "versions/*" else run(cmd)
