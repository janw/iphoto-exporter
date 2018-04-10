#!/usr/bin/env python3

import argparse
import plistlib
from os import path, makedirs
from shutil import copyfile
from slugify import slugify
from tqdm import tqdm

ALBUM_FILENAME = 'AlbumData.xml'
INPUT_DIRECTORY = '/mnt/home/Pictures/iPhoto/iPhoto Library'
OUTPUT_DIRECTORY = '/mnt/home/Pictures/iPhotoExport'
IGNORED_ALBUMS = ['flaggedAlbum', 'lastNMonthsAlbum', 'lastImportAlbum', ]


def export_iphoto(args):

    with open(path.join(INPUT_DIRECTORY, ALBUM_FILENAME), 'rb') as fp:
        data = plistlib.load(fp)
        masters = data.get('Master Image List')

    albums = [a for a in data['List of Albums']
              if a['GUID'] not in IGNORED_ALBUMS]

    for album in tqdm(albums):
        album_directory = path.join(OUTPUT_DIRECTORY, slugify(album['AlbumName']))
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

            full_source_path = path.join(
                INPUT_DIRECTORY, 'Masters', image_path)
            full_dest_path = path.join(
                album_directory, slugify(photo_key + '__' + image_filename))

            try:
                copyfile(full_source_path, full_dest_path)
            except FileNotFoundError:
                pass


parser = argparse.ArgumentParser(
    description='Export master images from an iPhoto Library.')
parser.add_argument('-i', '--input', required=True,
    help='''Path to the iPhoto Library to be exported''')
parser.add_argument('-o', '--output', required=True,
    help='''Base of the output path to which the albums are exported''')
parser.add_argument('-a', '--all', action='store_true',
    help='''If set, an album containing all photos will be created as well''')

if __name__ == '__main__':
    args = parser.parse_args()

    if not args.all:
        IGNORED_ALBUMS.append('allPhotosAlbum')

    INPUT_DIRECTORY = args.input
    OUTPUT_DIRECTORY = args.output

    export_iphoto(args)
