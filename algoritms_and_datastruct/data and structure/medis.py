class Node:
    def __init__(self, obj_name, is_dir, size=None, parent=None):
        self.obj_name = obj_name
        self.is_dir = is_dir
        self.size = size
        self.parent = parent
        self.children = {}

    def __repr__(self):
        return f"<Node {self.obj_name}; {self.is_dir}; {self.size}>"

    # def add_branch(self, branch):
    #     print('original branch definition:', branch)
    #     names = branch.split(".")
    #     print('*** names:', names)
    #     parent = self
    #     for name in names:
    #         if name not in parent.children:
    #             parent.add_child(Node(name))
    #         parent = parent.children[name]
    def add_child(self, node):
        print('parent node:', self)
        node.parent = self
        self.children[node.obj_name] = node
        print('children:', self.children)
        print('=' * 50)


# create root dir node
root_dir = Node(obj_name='/', is_dir=True)
print('root_dir', root_dir.children, root_dir.parent)
print('----------------------')
# root_dir = Node("/", True)
# create and connect home dir node
home = Node("home", True)
print('home', home.children, home.parent)
print('----------------------')
root_dir.add_child(home)
# raise Exception
# create and connect var dir node
# var = Node("var", True)
root_dir.add_child(var)
# create and connect log dir node
log = Node("log", True)
var.add_child(log)
# create and connect sys.log file node
sys_log = Node("sys.log", False, 10)
log.add_child(sys_log)
# root_dir.add_branch(kazkas)
# mammals = Node("mammals")
# # print(mammals)
# carnivora = Node("carnivora")
# # print(carnivora)
# mammals.add_child(carnivora)
# print(mammals.children)
#
# bears = Node("bears")
# carnivora.add_child(bears)
# print(carnivora.children)
#
#
# # mammals.add_branch("carnivora.felidae.panthera")
# # mammals.add_branch("carnivora.canidae.caninae")
# # mammals.add_branch("chiroptera.microchiroptera")
# #
# # print(mammals.children)
# # print(mammals.children["carnivora"].children)
# # print(mammals.children["carnivora"].children["canidae"].children)
