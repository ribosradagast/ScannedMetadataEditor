import os
import sys

from pyexiv2 import Image

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

path = sys.argv[1]
entries = os.scandir(path)

indexFile = open(path + "\\index.txt", mode="w", encoding="utf-8")

def get_image_description(path, metadata):
    if path.endswith('_b.jpg'):
        return metadata.get('Exif.Image.ImageDescription', 'delete')
    return metadata.get('Exif.Image.ImageDescription', '')

for entry in entries:
    if entry.name.endswith('.jpg'):
        i = Image(entry.path)
        metadata = i.read_exif()
        photo_date = metadata.get('Exif.Photo.DateTimeOriginal')
        description = get_image_description(entry.path, metadata)

        line = entry.name + '\n' + description + '\n' + photo_date
        print(line)
        indexFile.write(line + '\n')
