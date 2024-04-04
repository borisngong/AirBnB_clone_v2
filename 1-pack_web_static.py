#!/usr/bin/python3
"""
A Fabric script that generates a .tgz archive from the contents
of the web_static folder of the AirBnB Clone V2 repo.
Execute: fab -f 1-pack_web_static.py do_pack
"""

from datetime import datetime
from fabric.api import *


def do_pack():
    """
    Create an archive of the web_static folder.
    """

    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(archive))
    if create.failed:
        return None
    else:
        return 'versions/{}'.format(archive)
