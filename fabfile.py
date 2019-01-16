#!/usr/bin/env python
# init_py_dont_write_bytecode

#init_boilerplate

from fabric.api import *
from fabric.colors import *
from fabric.context_managers import *
from fabric.contrib.project import *


def buildAndDownload():
    local('make clean; make; make ESPPORT=/dev/ttyUSB0 flash')


def helloworld():
    # p.map(threaded_local,['id'])
    p = multiprocessing.Pool(int(total_cpu_threads))
    p.map(threaded_local, ['echo helloworld'] * 5000)
