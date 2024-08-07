from pathlib import Path
import logging
import os


logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Create the required directory under a parent directory

parent_directory = 'Classification'
dir_to_create = [
    # ".github/workflows/.gitkeep",
    f'src/{parent_directory}/__init__.py',
    f'src/{parent_directory}/components/__init__.py',
    f'src/{parent_directory}/utis/__init__.py',
    f'src/{parent_directory}/config/__init__.py',
    f'src/{parent_directory}/config/configuration.py',
    f'src/{parent_directory}/entity/__init__.py',
    f'src/{parent_directory}/pipeline/__init__.py',
    f'src/{parent_directory}/constants/__init__.py',
    "config.config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/traials.ipynb"
    
]

for filepath in dir_to_create:
    filepath = Path(filepath) # changing srt to os file path 
    
    dir, file_name = os.path.split(filepath) # splitting srt to dirname and file name 
    print(f"dir:{dir}", f"file: {file_name}")
    
    if dir != "":
        os.makedirs(dir, exist_ok=True)
        logging.info(f"created folder {dir} successfully ")
    else:
        logging.info("no directory name found")
        
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
            with open (filepath, 'w') as file:
                pass
                logging.info(f"files created {filepath}")
        
    else:
        logging.info(f"file already exists , filename: {filepath}")
