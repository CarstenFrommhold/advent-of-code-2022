import utils
from dataclasses import dataclass

data = utils.day_puzzle_to_list("07")


@dataclass
class Dir:
    folders: list
    files: list

    def __init__(self, folders=None, files=None):
        self.folders = folders
        self.files = files
        if self.folders is None:
            self.folders = []
        if self.files is None:
            self.files = []


@dataclass
class File:
    size: int
    name: str


dirs = dict()
pwd = "root"
ls_output = False
current_dir = "mock"

for cmd in data:

    if cmd == '$ cd /':
        continue
    elif cmd == '$ ls':
        ls_output = True
        current_dir = Dir()
        dirs[pwd] = current_dir
        continue
    elif cmd[:7] == "$ cd ..":
        pwd = "/".join(pwd.split("/")[:-1])
        continue
    elif cmd[:4] == "$ cd":
        folder = cmd[5:]
        pwd = pwd + "/" + folder
        ls_output = False
        continue

    if ls_output:
        if cmd[:3] == "dir":
            current_dir.folders.append(cmd.replace("dir ", ""))
        else:
            size, name = cmd.split(" ")
            size = int(size)
            current_dir.files.append(File(size, name))
        continue


def get_size(pwd, dir_):
    size = sum(file.size for file in dir_.files)
    subfolders = dir_.folders
    for subfolder in subfolders:
        subdir_pwd = pwd + "/" + subfolder
        subdir = dirs.get(subdir_pwd)
        if subdir is None:
            raise Exception
        size += get_size(subdir_pwd, subdir)
    return size


size = 0
at_most = 100000
for pwd, dir_ in dirs.items():
    size_dir = get_size(pwd, dir_)
    if size_dir <= at_most:
        size += size_dir

pt1 = size

# Pt Two
dirs_sizes = dict()
for pwd, dir_ in dirs.items():
    dirs_sizes[pwd] = get_size(pwd, dir_)

total_size = 70000000
current_space = total_size - dirs_sizes["root"]
needed_space = 30000000
to_be_free = abs(current_space - needed_space)

candidates = []
for dir_size in dirs_sizes.values():
    if dir_size > to_be_free:
        candidates.append(dir_size)

pt2 = min(candidates)

print("Part1:", pt1)
print("Part2:", pt2)
