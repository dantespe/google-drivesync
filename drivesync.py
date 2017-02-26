'''
NOTE: THIS VERSION OF DRIVESYNC 0.0.1
is still in beta and has only been
tested on Mac OS X 10.11.6
'''

import os
import shutil
import subprocess
import datetime


#Place the directories that you want synced
#here. Should be absolute paths
SYNC = [
    '/home/dante/Documents/'
]

#This is the directory of you google drive
GOOGLE = "~/Google Drive"

#The Folder your files will be saved under within GOOGLE drive
COMPUTER_NAME = '/Personal Laptop/'

#Where files are writting to
LOGS = '~/.Google/logs.txt'

CONTANCT = None

ERROR_MSG = ""

def copytree(src, dst, symlinks=False, ignore=None):
    if not os.path.exists(dst):
        os.makedirs(dst)

    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copytree(s, d, symlinks, ignore)
        else:
            if not os.path.exists(d) or os.stat(s).st_mtime != os.stat(d).st_mtime:
                shutil.copy2(s, d)

def make_dirs(directories):
    dirs = []

    for d in directories:
        dirs.append(d.split('/')[3])

    for d in dirs:
        temp = GOOGLE + COMPUTER_NAME + d
        if not os.path.isdir(temp):
            os.makedirs(temp)

def create_logs():
    #File is already created
    if os.path.isfile(LOGS):
        return

    #Parent dir but no file
    if os.path.isdir(LOGS.split('logs.txt')[0]) and \
        not os.path.isfile(LOGS):
        try:
            subprocess.call(["touch", LOGS])
        except:
            err = 'ERROR: File could not be made at: %s \n' % (LOGS)

    #Needs both .Google and logs.txt
    else:
        try:
            dirs = LOGS.split('logs.txt')[0]
            dirs = dirs[:-1]
            os.makedirs(dirs)
        except:
            err = 'ERROR: File could not be made at: %s' % (LOGS)

def migrate(directories):
    for dirs in directories:
        temp = os.listdir(dirs)
        files = []

        for file in temp:
            #Sees if file is hidden
            if os.path.isdir(dirs + file) and file[0] != '.' \
                and file[0] != '~':
                files.append(dirs + file + '/')

            elif file[0] != '.':
                files.append(dirs + file)

        for file in files:
            if os.path.isdir(file):
                dirs = GOOGLE + COMPUTER_NAME + file.split('/')[3] \
                    + '/' + file.split('/')[4] + '/'

                try:
                    copytree(file, dirs)
                except:
                    logs = open(LOGS, 'a+')
                    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                    ERROR = 'ERROR syncing %s on %s' % (file, date) + '\n'
                    logs.write(ERROR)
                else:
                    dirs = GOOGLE + COMPUTER_NAME + file.split('/')[3] \
                        + '/' + file.split('/')[4]

                try:
                    shutil.copy2(file, dirs)
                except:
                    logs = open(LOGS, 'a+')
                    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                    ERROR = 'ERROR syncing %s on %s' % (file, date) + '\n'
                    logs.write(ERROR)

def check_logs(errors):
    if errors != '':
        subject = 'ERRORS with drivesync on %s' % (COMPUTER_NAME)
        #notify(CONTANCT, errors, subject=subject)

def main():
    make_dirs(SYNC)
    create_logs()
    migrate(SYNC)

if __name__ == '__main__':
	main()
