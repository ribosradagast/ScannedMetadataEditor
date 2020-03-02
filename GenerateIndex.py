import os
import sys

from PIL import Image


def get_date_taken(path):
    return Image.open(path)._getexif()[36867]


def get_image_description(path):
    if path.endswith('_b.jpg'):
        return Image.open(path)._getexif().get(0x010e, 'delete')
    return Image.open(path)._getexif().get(0x010e, '')


print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

path = sys.argv[1]
entries = os.scandir(path)

indexFile = open(path + "\\index.txt", mode="w", encoding="utf-8")

entries = os.scandir(sys.argv[1])
for entry in entries:
    if entry.name.endswith('.jpg'):
        line = entry.name + '\n' + get_image_description(entry.path) + '\n' + get_date_taken(entry.path)
        print(line)
        indexFile.write(line + '\n')

