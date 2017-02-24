import filecmp
import os
import shutil
import subprocess
import datetime

""" This tool should work out of the box
    with version of Mac and Linux. With
    Linux you will need to install the
    all the dependencies for the Google API
    client. """

######### CONFIG ##############
#Place the directories that you want synced
#here. Should be absolute paths
SYNC = [
    'Documents/'
    'Desktop/'
]

#This is the directory of you google drive
#Should Have a trailing /
GOOGLE_DIR = "~/Google Drive/"

#The Folder your files will be saved under within GOOGLE drive
COMPUTER_NAME = '/Personal Laptop/'

#Where files are writting to
LOGS = '~/.Google/logs.txt'

#A snapshot of your current setup
CURRENT_DIR = "Current/"

#OLD FILES would be placed her
OLD_DIR = "Archive/"

#All files that start with these characters will not be synced
FORBIDDEN_LEAD_CHARS = [
    '~',
    '*'
]

def can_send(path):
    """ Checks to see if file starts with a FORBIDDEN_LEAD_CHARS character """
    filename = path.split('/')[-1]

    if filename[0] not in FORBIDDEN_LEAD_CHARS:
        return True
    return False

def get_full_path(relative, google=False):
    """ Returns the full path of any relative path based
        off of if local or not """
    if not google:
        return os.path.expanduser('~') + '/' + relative
    return GOOGLE_DIR + relative

def clean_up(path):
    """ takes relative local path recursively checks
        to see if each GOOGLE PATH follows the <CURRENT_DIR>/ <OLD_DIR>/
        structure """
    pass

def go_foward(local_path, google_path):
    """ Foward (returning True): local -> Google Drive
        Backward (returning False): Google Drive --> local
        Same File (returning None): <skip this file/dir> """
    pass

def get_file_metadata(path):
    """ Return a dictionary with all of the files meta data """
    pass

def send_file(src, dest):
    """ sends src to dest """
    pass

def sync_files(directories):
    for dirs in directories:
        clean_up(dirs)


def main():
    sync_files(SYNC)


main()
