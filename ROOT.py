import os

def GetRoot():
    return os.geteuid() == 0

def RunWithRoot(program):
    os.system("sudo {}".format(program))

def RUnWithRootGUI(program):
    os.system("pkexec {}".format(program))