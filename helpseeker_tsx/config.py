# AUTOGENERATED! DO NOT EDIT! File to edit: config.ipynb (unless otherwise specified).

__all__ = ['config_file_path', 'f', 'config']

# Comes from TSXCore.ipynb, cell
from pathlib import Path
import json

config_file_path = Path("config.json")
f = open(config_file_path,"r")
config = json.load(f)