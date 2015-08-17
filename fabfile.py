from fabric.api import env
from fabric.api import put
from fabric.api import quiet
from fabric.api import sudo
import time

env.hosts = ["133.242.133.41"]
env.user = "kitak"

def deploy():
    with quiet():
        sudo('mkdir /usr/local/kitak.info')

    put('./public/*', '/usr/local/kitak.info', mirror_local_mode=True, use_sudo=True)
