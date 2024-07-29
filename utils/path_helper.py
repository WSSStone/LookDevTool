import os

def handle_spaced_dir(argv:list) -> str:
    res = ''
    n = len(argv)
    for i in range(1, n):
        res += argv[i]
        if i != n - 1:
            res += ' '
    return f'{res}'

class path_node:
    def __init__(self, path:str, prt=None) -> None:
        self.path = path
        self.parent = prt
        self.isfile = os.path.isfile(self.path)
        self.children = []

    def add_child(self, child) -> None:
        child.parent = self
        self.children.append(child)

    def emplace_child(self, child_path:str):
        ch = path_node(child_path)
        self.add_child(ch)
        return ch

class path_tree:
    def __init__(self, root_path:str) -> None:
        self.root = path_node(root_path)
        self._recur_iter(self.root)

    def _recur_iter(self, node:path_node) -> None:
        _dir = node.path
        li = os.listdir(_dir)
        for p in li:
            _path = os.path.join(_dir, p)
            _node = node.emplace_child(_path)
            if os.path.isdir(_path):
               self._recur_iter(_node)

    def node_task(self, node:path_node, func) -> None:
        func(node)
        for ch in node.children:
            if ch.isfile:
                func(ch)
            else:
                self.node_task(ch, func)

if __name__ == '__main__':
    template_dir = "E:/Work/ExternalAssets/scripts/template/PluginTemplate/Plugin"
    
    ptree = path_tree(template_dir)

    def print_node(node) -> None:
        print(node.path)

    ptree.node_task(ptree.root, print_node)
