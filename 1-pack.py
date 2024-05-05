#!/usr/bin/env python3

from fabric.api import *

def do_pack():
    local('sudo mkdir -p versions')
