from typing import List, Optional, Tuple

from dataclasses import dataclass

def get_input(file_name: str):
    input = None
    with open(file_name) as f:
        input = f.readlines()
    input = [line.replace("\n", "") for line in input]
    return input

@dataclass
class FileNode():
    name: str
    size: int

@dataclass
class DirectoryNode():
    name: str
    parent_directory: Optional["DirectoryNode"] = None
    files: Optional[List[FileNode]] = None
    directories: Optional[List["DirectoryNode"]] = None

    def add_file(self, name: str, size: int):
        if not self.files:
            self.files = []
            
        self.files.append(FileNode(name=name, size=size))

    def add_directory(self, name: str):
        if not self.directories:
            self.directories = []
        self.directories.append(DirectoryNode(name=name, parent_directory=self))

    def get_child_directory(self, name:str):
        for directory in self.directories:
            if directory.name == name:
                return directory

    def get_directory_size(self) -> int:
        size = 0
        if self.files:
            size += sum([f.size for f in self.files])
        if self.directories:
            size += sum([d.get_directory_size() for d in self.directories])
        return size

    def get_directories_under_size(self, max_size: int):
        dirs = []
        if self.directories:
            dirs.extend([d for d in self.directories if d.get_directory_size() <= max_size])
            for d in self.directories:
                dirs.extend(d.get_directories_under_size(max_size))
        return dirs

    def get_directories_over_size(self, min_size: int):
        dirs = []
        if self.directories:
            dirs.extend([d for d in self.directories if d.get_directory_size() >= min_size])
            for d in self.directories:
                dirs.extend(d.get_directories_over_size(min_size))
        return dirs

def build_directory_tree(input):
    base_directory = None
    current_directory = None
    for line in input:
        if "$ " in line:
            command = command_arg = None
            full_command = line.replace("$ ", "").split(" ")
            command = full_command[0]
            if len(full_command) > 1:
                command_arg = full_command[1]

            match command:
                case "cd":
                    if command_arg == "..":
                        current_directory = current_directory.parent_directory
                    else:
                        if not base_directory:
                            first_node = DirectoryNode(name=command_arg)
                            base_directory = first_node
                            current_directory = first_node
                        else:
                            current_directory = current_directory.get_child_directory(name=command_arg)
        else:
            if "dir" in line:
                dir_properties = line.split(" ")
                current_directory.add_directory(name=dir_properties[1])
            else:
                file_properties = line.split(" ")
                current_directory.add_file(name=file_properties[1], size=int(file_properties[0]))
    return base_directory


def part_1():
    input = get_input("src/2022/12-7/input.txt")
    base_directory = build_directory_tree(input)
    max_size = 100000
    directories_under_size = []
    if base_directory.get_directory_size() <= max_size:
        directories_under_size.append(base_directory)
    directories_under_size.extend(base_directory.get_directories_under_size(max_size))
    
    return sum([d.get_directory_size() for d in directories_under_size])


def part_2():
    input = get_input("src/2022/12-7/input.txt")
    base_directory = build_directory_tree(input)
    max_size = 70000000
    size_goal = 30000000
    current_used = max_size - base_directory.get_directory_size()
    needed_space = size_goal-current_used

    directories_over_size = []
    if base_directory.get_directory_size() >= needed_space:
        directories_over_size.append(base_directory)
    directories_over_size.extend(base_directory.get_directories_over_size(needed_space))

    return min([d.get_directory_size() for d in directories_over_size])


print(part_1(), part_2())
