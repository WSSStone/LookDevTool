import os, sys
from utils.path_helper import handle_spaced_dir
from utils.cmds_library import cmd_fab

def generate_sln(proj_absname:str):
    cmd = cmd_fab.fabric_generate_sln_cmd(proj_absname)
    print(cmd)
    print(os.system(cmd))

def main(argv):
    if len(argv) < 2:
        print("Empty Input")
        return
    
    work_dir = handle_spaced_dir(argv)
    template_dir = os.path.realpath("./template/ProjectModuleTemplate/")
    os.chdir(work_dir)

    proj_name = None
    for f in os.listdir("."):
        if ".uproject" in f:
            proj_name = f.split('.')[0]

    if proj_name is None:
        return

    proj_absname = f'{os.path.join(work_dir, proj_name)}.uproject'
    
    generate_sln(proj_absname)

if __name__ == '__main__':
    main(sys.argv)