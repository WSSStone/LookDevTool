import os, sys
from utils.path_helper import handle_spaced_dir
from utils.cmds_library import cmd_fab

TARGET_PROJ_DIR = "D:/Work/MII/Project/"
TARGET_CONTENT_DIR = os.path.join(TARGET_PROJ_DIR, "Content")
TARGET_PLUGIN_DIR = os.path.join(TARGET_PROJ_DIR, "Plugins")

def link_content(work_dir:str, dirname:str):
    cmd = cmd_fab.fabric_softlink_cmd(TARGET_CONTENT_DIR, work_dir, dirname)
    print(cmd)
    os.system(cmd)

def link_nextlevel_content(work_dir:str, dirname:str):
    _work_dir = os.path.join(work_dir, dirname)
    os.chdir(_work_dir)
    for p in os.listdir(_work_dir):
        if not (os.path.isdir(os.path.join(_work_dir, p))):
            continue
        link_content(_work_dir, p)
    os.chdir(work_dir)

def link_plugin(work_dir:str, dirname:str):
    _work_dir = os.path.join(work_dir, dirname)
    os.chdir(_work_dir)
    cmd = cmd_fab.fabric_softlink_cmd(TARGET_PLUGIN_DIR, work_dir, dirname)
    os.chdir(work_dir)
    print(cmd)
    os.system(cmd)

def main(argv:list):
    if len(argv) < 2:
        print("Empty Input")
        return
    
    WORK_DIR = handle_spaced_dir(argv)
    os.chdir(WORK_DIR)

    for p in os.listdir(WORK_DIR):
        if not (os.path.isdir(os.path.join(WORK_DIR, p))):
            continue

        if 'nextlevel' in p:
            link_nextlevel_content(WORK_DIR, p)
            continue

        if 'plugin' in p:
            if not os.path.exists(TARGET_PLUGIN_DIR):
                os.mkdir(TARGET_PLUGIN_DIR)
            link_plugin(WORK_DIR, p)
            continue

        if 'Proj' in p:
            print('ignore')
            continue

        link_content(WORK_DIR, p)
        

if __name__ == '__main__':
    main(sys.argv)