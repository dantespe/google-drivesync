import filecmp, os
import shutil, subprocess, datetime

######### CONFIG ##############
#Place the directories that you want synced
#here. Should be absolute paths
SYNC = [
    'Documents/',
    'Desktop/'
]

#This is the directory of you google drive
#Should Have a trailing /
GOOGLE_DIR = "Google Drive/"

#The Folder your files will be saved under within GOOGLE drive
COMPUTER_NAME = 'Personal Laptop/'

#A snapshot of your current setup
CURRENT_DIR = "Current/"

#OLD FILES would be placed here
OLD_DIR = "Archive/"

#All files that start with these characters will not be synced
FORBIDDEN_LEAD_CHARS = [
    '~',
    '*'
]

#### Drive Hints
### a file named !sync_to_local created on Google Drive would sync down to your
## local computer as sync_to_local and back to drive as sync_to_local
DRIVE_HINTS = [
    '!'
]

def get_filename(path):
    """ Takes in a file input """
    return path.split('/')[-1]

def can_send(path, google=False):
    """ Checks to see if file starts with a FORBIDDEN_LEAD_CHARS character """
    filename = get_filename(path)
    if google and filename[0] in DRIVE_HINTS:
        return True
    if filename[0] not in FORBIDDEN_LEAD_CHARS:
        return True
    return False

def get_full_path(relative, google=False):
    """ Returns the full path of any relative path based
        off of if local or not """
    home_dir = os.path.expanduser('~')
    if not google:
        return  os.path.join(home_dir, relative)
    return os.path.join(home_dir, GOOGLE_DIR + COMPUTER_NAME + relative)

def clean_up(path):
    """ takes relative local path recursively checks
        to see if each GOOGLE PATH follows the <CURRENT_DIR>/ <OLD_DIR>/
        structure """
    correct_struct = [CURRENT_DIR, OLD_DIR]
    google_full_path = get_full_path(path, google=True)

    files = os.listdir(google_full_path)
    ##Fixes current path
    if files != correct_struct:
        correct_structure(google_full_path)

    #### recursively fix and copy sub directories #####
    for f in files:
        temp_file = os.path.join(google_full_path, f)
        if os.path.isdir(temp_file):
            clean_up(os.path.join(path, f))

def correct_structure(google_full_path):
    try:
        os.makedirs(os.path.join(google_full_path, CURRENT_DIR))
    except OSError:
        pass #already exists
    try:
        adir = os.path.join(google_full_path, OLD_DIR)
        os.makedirs(adir)
    except OSError:
        pass

    for f in files:
        subprocess.call(["cp", "-r", f, adir])

def go_foward(local_path, google_path):
    """ Foward (returning True): local -> Google Drive
        Backward (returning False): Google Drive --> local ##YOU NEED TO SPECFY HINT
        Same File (returning None): <skip this file/dir> """
    if os.path.isdir(local_path) and os.path.isdir(google_path):
        pass

    temp = os.listdir(local_path)
    local_files = [x for x in temp if not os.path.isdir(x)]
    temp = os.listdir(google_path)
    google_files = [x for x in temp if not os.path.isdir(x)]

    #checking for foward and backwards with the same file
    for lfile in local_files:
        if lfile in google_files:
            lfilename = os.path.join(local_path, lfile)
            gfilename = os.path.join(google_path, lfile)

            if not filecmp.cmp(lfilename, gfilename):
                ltimestamp = os.path.getmtime(lfilename)
                gtimestamp = os.path.getmtime(gfilename)

            print "ltimestamp: %s" % (ltimestamp)
            print "gtimestamp: %s" % (gtimestamp)
    #checking for backwards

def go_foward_dir_helper(local_dir, google_dir):
    pass

def send_file(src, dest, archive=False):
    """ sends src to dest if can_send_src"""
    pass

def sync_files():
    for dirs in SYNC:
        clean_up(dirs)

def main():
    #sync_files()
    pass

main()
