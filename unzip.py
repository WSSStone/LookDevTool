import os, sys
from utils.path_helper import handle_spaced_dir
from utils.cmds_library import cmd_fab

EXTENSIONS = ["zip", "7z", "rar"]

def get_extension(path:str) -> str:
    return path.split('.')[-1]

def get_native_name(path:str) -> str:
    length = len(path)

    idx = length - 1
    for i in range(length):
        idx = length - 1 - i
        if path[idx] == '.':
            return path[0:idx:1]
        
    return path

def rename_to_ascii(abspath:str) -> str:
    newname = ''
    for char in abspath:
        if char.isascii():
            newname += char
    if len(newname) != len(abspath):
        os.rename(abspath, newname)
    return newname

def unzip_recur(work_dir:str, cur_dir:str) -> None:
    os.chdir(work_dir)

    li = os.listdir(work_dir)
    for p in li:
        abspath = os.path.join(work_dir, p)

        if not os.path.exists(abspath):
            continue

        if not os.path.isfile(abspath):
            unzip_recur(abspath, work_dir)

        if get_extension(p) not in EXTENSIONS:
            continue

        print(abspath)
        abspath = rename_to_ascii(abspath)
        print(abspath)
        cmd = cmd_fab.fabric_unzip_cmd(abspath, get_native_name(abspath))
        print(cmd)
        
        os.chdir(work_dir)
        print(os.system(cmd))

    os.chdir(cur_dir)

def main(argv):
    if len(argv) < 2:
        print("Empty Input")
        return
    
    work_dir = handle_spaced_dir(argv)
    
    unzip_recur(work_dir, work_dir)

if __name__ == '__main__':
    main(sys.argv)