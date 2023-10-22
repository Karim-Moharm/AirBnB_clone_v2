#!/usr/bin/python3
"""the __init__ module
"""
import os
from models.engine.file_storage import FileStorage


if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
