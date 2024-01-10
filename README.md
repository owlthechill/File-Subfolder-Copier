## Overview

This simple Python program is designed to copy a list of source files from a common folder to a destination folder while preserving the subfolder structure. It allows users to set the depth of the folders to be copied.

## Features

- Copies specified files from a source folder to a destination folder.
- Preserves the subfolder structure up to a specified depth. (e.g. one/two/three/four/five, where a depth of two will not preserve the ``one`` folder)
- Customizable depth parameter to control how deep into the directory structure the program will copy files, maxing out at the shallowest folder structure found.

## Requirements

- Python 3.x
- `shutil` library (included in the Python standard library)
- `rich` library (version 13.7.0, not included in the Python standard library)

## Usage

1. Clone or download the repository.

2. Open a terminal and navigate to the project directory.

3. Run the script with the following command:

    ```bash
    python copy_files.py
    ```

4. Follow the on-screen prompts to provide the list of source files, set the source folder, destination folder, and specify the depth.

## Example

```bash
python copy_files.py
