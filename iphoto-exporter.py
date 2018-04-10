#!/usr/bin/env python3

import plistlib
from os import path, makedirs
from shutil import copyfile

ALBUM_FILENAME = 'AlbumData.xml'
INPUT_DIRECTORY = '/mnt/home/Pictures/iPhoto/iPhoto Library'
OUTPUT_DIRECTORY = '/mnt/home/Pictures/iPhotoExport'


_file_object = None

with open(path.join(INPUT_DIRECTORY, ALBUM_FILENAME), 'rb') as fp:
    data = plistlib.load(fp)
    masters = data.get('Master Image List')

for album in data['List of Albums']:
    if album['GUID'] not in ['allPhotosAlbum', 'flaggedAlbum', 'lastNMonthsAlbum', 'lastImportAlbum', ]:
        album_directory = path.join(OUTPUT_DIRECTORY, album['AlbumName'])
        makedirs(album_directory, exist_ok=True)

        for photo_key in album['KeyList']:
            master_element = masters.get(photo_key, None)

            if master_element is None:
                print(photo_key, 'not in Masters')
                continue

            image_path = master_element.get('ImagePath').split('Masters/')[-1]
            if image_path.startswith('/'):
                continue
            image_filename = path.basename(image_path)

            full_source_path = path.join(INPUT_DIRECTORY, 'Masters', image_path)
            full_dest_path = path.join(album_directory, photo_key + '__' + image_filename)
            print(full_source_path)
            print(full_dest_path)
            copyfile(full_source_path, full_dest_path)


        break

