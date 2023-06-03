import os
from pathlib import Path


def read_token_file() -> str:
    access_token_path: Path = Path.home() / 'dropbox-tools' / 'access_token.txt'
    if not Path.exists(access_token_path):
        if not Path.exists(access_token_path.parent):
            access_token_path.parent.mkdir()
        access_token_file = open(access_token_path, 'w')
        access_token_file.close()
    access_token_file = open(access_token_path, 'r')
    output = access_token_file.readline()
    access_token_file.close()
    return output.strip()
