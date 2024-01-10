from tkinter import filedialog as fd
from rich.prompt import Prompt
from rich import print
import os
import shutil


def get_file_path():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    filetypes = (('text files', '*.txt'),('All files', '*.*'))
    filename = fd.askopenfilename(title='Open a file', initialdir=dir_path,filetypes=filetypes)
    return filename

rainbow_colors = ['red', 'yellow', 'green', 'blue', 'violet']

def read_paths_from_file(filename):
    paths = []
    max_depth = 100
    example_paths = []
    
    with open(filename, 'r') as file:
        for line in file:
            path = line.strip()
            # Process each path as needed
            print(f"Processing path: {path}")
            path_components = path.split(os.sep)
            paths.append(path_components)
            if len(path_components) < max_depth:
                max_depth = len(path_components)
                example_paths = path_components

    print(f"Max depth: {max_depth}")
    return paths, example_paths, max_depth

def format_depth_string(example_paths, rainbow_colors):
    depth_str = ""
    for i, path_component in enumerate(example_paths[1:]):
        separator = '\\\\' if i < len(example_paths) - 1 else ''
        depth_str += f"[{rainbow_colors[i % len(rainbow_colors)]}] {path_component}{separator}"
    return depth_str

def get_destination_folder():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    folder = filename = fd.askdirectory(title='Select destination folder', initialdir=dir_path)
    return folder

def get_depth():
    try:
        depth = int(Prompt.ask("Enter path depth"))
        return depth
    except ValueError:
        print(f"Invalid integer, max depth is {max_depth}")

def copy_files(paths, depth, max_depth, dir_path):
    if depth >= max_depth:
        print(f"Exceeded max depth of {max_depth}")

    for path in paths:
        # make directory list to clip off extra directory folders plus file
        directory = path[depth:-1]

        # get file name
        file = path[-1]

        # construct path for source file path to copy from
        source_path = os.path.join(*path)

        # construct path for destination folders
        full_path = os.path.join(dir_path, *directory)
        os.makedirs(full_path, exist_ok=True)

        # construct destination file path
        dest_path = os.path.join(full_path, file)

        # copy source file to destination file path
        print(f"{source_path} to {dest_path}")
        # shutil.copy(source_path, dest_path)


if __name__ == "__main__":
    filename = get_file_path()
    paths, example_paths, max_depth = read_paths_from_file(filename)
    depth_str = format_depth_string(example_paths, ['red', 'yellow', 'green', 'blue', 'violet'])
    print(depth_str)

    folder = get_destination_folder()
    depth = get_depth()
    copy_files(paths, depth, max_depth, folder)