from dropbox.files import FileMetadata

from common_utils import read_token_file
import dropbox
import re

dated_file_regexp = "(\d{4})-(\d{2})-(\d{2}) \d{2}.\d{2}.\d{2}"


def organize_files_by_year():
    token: str = read_token_file()
    dbx = dropbox.Dropbox(token)
    result = dbx.files_list_folder('/Camera Uploads')
    # gather all files in the 'Camera Uploads' directory and figure out the year
    file_count = 0
    files_to_move = {}
    while result is not None:
        file_count = file_count + len(result.entries)
        print(f'Found {file_count} files')
        entry: FileMetadata
        for entry in result.entries:
            match_object = re.search(dated_file_regexp, entry.name)
            if match_object is not None:
                files_to_move[entry.name] = match_object.group(1)
        if result.has_more:
            result = dbx.files_list_folder_continue(result.cursor)
        else:
            result = None
    # move each file you found into the year directory it belongs
    moved_count = 0
    for file_name, folder_name in files_to_move.items():
        source = f'/Camera Uploads/{file_name}'
        destination = f'/Camera Uploads/{folder_name}/{file_name}'
        relocation_result = dbx.files_move_v2(source, destination)
        print(f'Moved {source} to {destination}!')
        moved_count = moved_count + 1
        print(f'{round(moved_count / file_count * 100, 2)}% complete...')
    print(f'Finished!')
    

if __name__ == "__main__":
    organize_files_by_year()
