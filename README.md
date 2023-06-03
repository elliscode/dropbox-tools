# Dropbox Tools

## How to set your access token

- navigate to your home directory &mdash; `cd ~`
- create a folder called `dropbox-tools` in your home directory &mdash; `mkdir dropbox-tools`
- change directory into the new folder &mdash; `cd dropbox-tools`
- create a file in this directory called `access_token.txt` &mdash; `touch access_token.txt`
- paste your access token that you generate by [following this guide](https://dropbox.tech/developers/generate-an-access-token-for-your-own-account) into your newly created `~/dropbox-tools/access_token.txt` file

## Camera Uploads Yearly Folder Organizer

Code lives in in `dated_file_organizer.py`

- looks at all the photos in the `/Camera Uploads/` directory in dropbox
- searches for `yyyy-MM-dd hh.mm.ss` anywhere in the filename
- if found, moves each file into a folder with the year, `/Camera Uploads/yyyy/`
- this makes it easier to navigate the camera uploads folder

does not move pictures taken in the current year, as I didn't want our phones and tables to re-upload photos into the camera uploads folder