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
        
        if os.system(cmd) is 0:
            print(f'{abspath} successfully unzipped. Now removing zip file.')

            def _error_log(func, path, excinfo):
                """
                Function that track and record the errors when removing files/dirs

                Args:
                    func (function): The function that raised the error.
                    path (string): Path to the file/dir that raised the error.
                    excinfo (tuple): The exception information returned by sys.exc_info().
                """

                # Log dict -> key= file/dir fullpath: value= [error class, error message, function that raised the error] 
                log = {}
                # Set the file/dir full path as key with an empty list as value
                log.setdefault(path, [])

                # Append the error class and message raised from excinfo tuple
                log[path].append(excinfo[0].__name__)
                log[path].append(excinfo[1].strerror)

                # Append the function that raised the error
                log[path].append(func.__name__)

                return log
            
            import shutil
            shutil.rmtree(abspath, onerror=_error_log)

    os.chdir(cur_dir)

def main(argv):
    if len(argv) < 2:
        print("Empty Input")
        return
    
    work_dir = handle_spaced_dir(argv)
    
    unzip_recur(work_dir, work_dir)

if __name__ == '__main__':
    main(sys.argv)