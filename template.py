import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

projet_name = "text_summarizer"

list_of_files = [
    ".github.com/workflow/.gitkeep",
    f"src/{projet_name}/__init__.py",
    f"src/{projet_name}/components/__init__.py",
    f"src/{projet_name}/utils/__init__.py",
    f"src/{projet_name}/utils/common.py",
    f"src/{projet_name}/logging//__init__.py",
    f"src/{projet_name}/config/configuration.py"
    f"src/{projet_name}/pipeline/__init__.py",
    f"src/{projet_name}/entity/__init__.py",
    f"src/{projet_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb"


]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory:{filedir} for the file {filename}")

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"creating empty file:{filepath}")


    else:
        logging.info(f"{filename} is already exists")

