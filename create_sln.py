import os, sys
from utils.path_helper import handle_spaced_dir
from utils.cmds_library import cmd_fab
from generate_sln import generate_sln

FILE_CNT = 5

def copy_content(src:str, dst:str, module_name:str) -> None:
    content = ""
    
    with open(src, "r+") as srcf:
        content = srcf.readlines()
    srcf.close()

    for i in range(len(content)):
        content[i] = content[i].replace("Template", module_name)

    with open(dst, "w+") as dstf:
        dstf.writelines(content)
    dstf.close()

def get_names(inp:str) -> list:
    return [f"{inp}.Target.cs", f"{inp}Editor.Target.cs",
            f"{inp}/{inp}.h", f"{inp}/{inp}.cpp", f"{inp}/{inp}.build.cs"]

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
    
    source_name = f"./Source/"
    if not os.path.exists(source_name):
        os.mkdir(source_name)

    os.chdir(source_name)

    module_dir = f"./{proj_name}/"
    if not os.path.exists(module_dir):
        os.mkdir(module_dir)

    template_files = [os.path.join(template_dir, f) for f in get_names("Template")]
    module_files = get_names(proj_name)

    for i in range(0, FILE_CNT):
        copy_content(template_files[i], module_files[i], proj_name)

    os.chdir(work_dir)

    proj_absname = f'{os.path.join(work_dir, proj_name)}.uproject'
    
    generate_sln(proj_absname)

if __name__ == '__main__':
    main(sys.argv)