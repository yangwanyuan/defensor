#!/usr/bin/env python
# -*- coding: utf-8 -*-
##############################################################################
# 
# Project   : Defensor
# Author    : Yy
# Email     : yangwanyuan@ztgame.com
# Date      : 2015.11 
#
##############################################################################

##############################################################################
# 
# Import system library from here
#
##############################################################################
import os
import sys

##############################################################################
# 
# Import project file from here
#
##############################################################################
from defensor.api.Api import load
from defensor.api.Api import get_api_params
from defensor.api.Api import app 
from defensor.common.DfsLog import log_set_up
from defensor.common.DfsConfig import DfsConfig

CONF = DfsConfig()

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

possible_topdir = os.path.normpath(os.path.join(os.path.abspath(sys.argv[0]),
                                   os.pardir,
                                   os.pardir))
if os.path.exists(os.path.join(possible_topdir, 'defensor', '__init__.py')):
    sys.path.insert(0, possible_topdir)


CONF.init_config("/etc/defensor/api.conf")
log_set_up("/var/log/defensor/api.log")
load()

application = app
if __name__ == "__main__":
    host, port, processes = get_api_params()
    app.run(host=host, port=port, processes=processes)
