# showu/app/utils/file_storage.py

import os
import shutil
from fastapi import UploadFile

UPLOAD_DIR = "uploads/"

def save_file(file: UploadFile, subdir: str = "misc") -> str:
    dir_path = os.path.join(UPLOAD_DIR, subdir)
    os.makedirs(dir_path, exist_ok=True)

    file_path = os.path.join(dir_path, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return file_path