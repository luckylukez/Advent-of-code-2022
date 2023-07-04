small_dirs = []
large_dirs = []
MIN_DELETE_SIZE = 8381165

class FolderTree():
    def __init__(self, root):
        self.root = root
        self.dir_sizes = []
        self.dirs = {}
        self.root.tree = self
        self.size = 0

    def get_min_delete_size(self, min_size):
        print(self.dir_sizes)
        big_size_list = []
        for size in self.dir_sizes:
            if size >= min_size:
                big_size_list.append(size)
        return min(big_size_list)
    
    def calculate_size(self):
        return self.root.calculate_size()

class FolderNode():
    def __init__(self, name, parent):
        self.tree = None
        self.name = name
        self.parent = parent
        if self.parent is not None:
            self.tree = self.parent.tree
        self.files = {} # Store file names and their sizes
        self.folders = {} # store folder nodes
        self.size = 0

    def add_file(self, name, size):
        self.files[name] = size
    
    def add_folder(self, name):
        full_name = self.name + '/' + name
        self.folders[full_name] = FolderNode(full_name, self) # Set self as parent

    def calculate_size(self):
        self.size += sum(self.files.values())
        self.size += sum([folder.calculate_size() for folder in self.folders.values()]) # Recursive call. 
        if self.size <= 100_000:
            small_dirs.append(self)
        elif self.size >= MIN_DELETE_SIZE:
            large_dirs.append(self)
        self.tree.dir_sizes.append(self.size)
        return self.size
    
# First build tree.

with open('data.txt', 'r') as data:
    lines = [line.strip() for line in data.readlines()]

root_node = FolderNode('/', None)
tree = FolderTree(root_node)
current_node = root_node

for line in lines:
    #print(line)
    if line[:4] == '$ cd':
        folder_name = line[5:]
        if folder_name in tree.dirs.keys():
            print(folder_name + "is jumped into more than once!!")
        else:
            if folder_name == '..':
                current_node = current_node.parent
            elif folder_name == '/':
                current_node = root_node
            else:
                dir_name = current_node.name + '/' + folder_name
                current_node = current_node.folders[dir_name]

    elif line[:4] == '$ ls':
        continue

    elif line[:4] == 'dir ':
        name = line[4:]
        current_node.add_folder(name)
    else:
        (size, name) = line.split(' ')
        size = int(size)
        current_node.add_file(name, size)

# Recursively calculate size of folders

total_space = 70_000_000
needed_space = 30_000_000

used_space = tree.calculate_size()
min_remove_size = used_space - (total_space - needed_space) 

actual_remove_size = tree.get_min_delete_size(min_remove_size)

small_dir_sum = sum([dir.size for dir in small_dirs])
min_large_dir = min([dir.size for dir in large_dirs])
print(small_dir_sum)
print(root_node.size)
print(actual_remove_size)


