from fabric.api import put, run


def prepare_server():
    run("mkdir -p ~/switcher")


def copy_server():
    put('../server', "~/switcher")


def remove_server():
    run('rm -rf ~/switcher/server')


def deploy():
    prepare_server()
    copy_server()


def clean():
    remove_server()
