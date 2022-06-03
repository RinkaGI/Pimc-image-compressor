import os, sys


windowsNames = {'win32', 'cygwin'}
linuxMacNames = {'linux', 'linux2', 'linux3', 'darwin', 'aix'}

print('Installing...')
if sys.platform is windowsNames:
        os.system('py -m pip install -r requeriments.txt')
elif sys.platform is linuxMacNames:
        os.system('pip3 install -r requirements.txt')
else:
        os.system('pip3 install -r requirements.txt')
