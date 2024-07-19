import os
from utils.cmds_library import fabric_unzip_cmd

WORK_DIR = "E:/Work/ExternalAssets/20240719/"
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

def main():
    li = os.listdir(WORK_DIR)
    for p in li:
        abspath = os.path.join(WORK_DIR, p)

        if not os.path.exists(abspath):
            continue

        if not os.path.isfile(abspath):
            continue

        if get_extension(p) not in EXTENSIONS:
            continue

        print(abspath)
        abspath = rename_to_ascii(abspath)
        print(abspath)
        cmd = fabric_unzip_cmd(abspath, get_native_name(abspath))
        print(cmd)
        
        os.chdir(WORK_DIR)
        print(os.system(cmd))

if __name__ == '__main__':
    main()