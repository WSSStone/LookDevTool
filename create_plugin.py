import os, sys, shutil
from utils.path_helper import *
from utils.cmds_library import cmd_fab

def main(argv:list):
    if len(argv) < 3:
        print("Invalid Input")
        return
    
    template_dir = os.path.realpath("./template/PluginTemplate/")
    PLUGIN_NAME = argv[2]
    argv.pop()
    work_dir = handle_spaced_dir(argv)

    os.chdir(work_dir)

    target_dir = os.path.join(work_dir, "Plugins")
    if not os.path.exists(target_dir):
        shutil.copytree(
            os.path.join(template_dir, "Plugins"),
            os.path.join(work_dir, "Plugins"))

    ptree = path_tree(target_dir)

    def cmd_semantics_mv(node:path_node) -> None:
        # rename
        if "Plugin.Build" in node.relpath:
            node.rename(PLUGIN_NAME + ".Build")

            with open(node.abspath, "r+") as rf:
                content = rf.readlines()
            rf.close()
            
            for line in content:
                line = line.replace("PLUGIN", PLUGIN_NAME)
                print(line)

            with open(node.abspath, "w+") as wf:
                wf.writelines(content)
            wf.close()

        elif "Module" in node.relpath or "Plugin" in node.relpath:
            node.rename(PLUGIN_NAME)
        else:
            node.udpate_path()            

    ptree.node_task(ptree.root, cmd_semantics_mv)

if __name__ == '__main__':
    main(sys.argv)