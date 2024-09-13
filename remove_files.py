import os, sys, shutil
from utils.path_helper import *

def remove_files(work_dir:str, rm_ext:list=[], reserve_ext:list=[]) -> None:
    ptree = path_tree(work_dir)

    if len(rm_ext) == 0 and len(reserve_ext) == 0:
            print("No specified extensions.")
            quit()
    
    def rm_file(node:path_node):
        if not node.isfile:
            return

        name, ext = os.path.splitext(node.abspath)
        if (len(rm_ext) > 0 and ext in rm_ext) or (len(reserve_ext) > 0 and ext not in reserve_ext):
            os.remove(node.abspath)

    ptree.node_task(ptree.root, rm_file)

    def clean_empty(node:path_node):
        if not node.isfile and len(os.listdir(node.abspath)) == 0:
            shutil.rmtree(node.abspath)

    ptree.node_task(ptree.root, clean_empty)

def main(argv):
    if len(argv) < 2:
        print("Empty Input")
        return
    
    work_dir = handle_spaced_dir(argv)

    remove_files(work_dir, rm_ext=['.uasset', '.umap'])

if __name__ == '__main__':
    main(sys.argv)
