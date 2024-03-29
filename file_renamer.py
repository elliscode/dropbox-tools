import re
import datetime
from pathlib import Path
import os
import shutil

dated_file_regexp = "(\d{4})-(\d{2})-(\d{2}) \d{2}.\d{2}.\d{2}"


def rename_all_files_to_date_created(input_path):
    destination_path = Path('~/Desktop/flip_phone_photos')
    if not os.path.exists(destination_path):
        destination_path.mkdir()
    for currentpath, folders, files in os.walk(input_path):
        current_path = Path(currentpath)
        for file in files:
            if not (file.endswith('.png')\
                    or file.endswith('.jpg')\
                    or file.endswith('.jpeg')\
                    or file.endswith('.mov')\
                    or file.endswith('.3gp')):
                continue
            unix_time = os.stat(current_path.joinpath(file)).st_birthtime
            print(f"{file} -- {unix_time}")
            destination_file_name = datetime.datetime.fromtimestamp(unix_time).strftime('%Y-%m-%d %H.%M.%S')
            destination_full_name = destination_file_name + file[file.rindex('.'):].lower()
            final_path = destination_path.joinpath(destination_full_name)
            print(final_path)
            shutil.copy(current_path.joinpath(file), final_path)
            print('copied')


if __name__ == "__main__":
    rename_all_files_to_date_created(Path('/Volumes/Untitled/'))
