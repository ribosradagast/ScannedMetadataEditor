import os
import sys

import piexif
from PIL import Image


def get_date_taken(path):
    return Image.open(path)._getexif()[36867]


def get_image_description(path):
    return Image.open(path)._getexif().get(0x010e, 'delete_this_file')


print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

path = sys.argv[1]
entries = os.scandir(path)

indexFile = open(path + "\\index.txt", mode="r", encoding="utf-8")
os.mkdir(path + "\\to_delete\\")

while True:
    fileName = indexFile.readline().strip()
    description = indexFile.readline().strip()
    dateTaken = indexFile.readline().strip()
    if not dateTaken: break  # EOF

    if description != 'delete':
        image = Image.open(path + "\\" + fileName)
        exif_dict = piexif.load(image.info["exif"])
        exif_dict["Exif"][36867] = dateTaken
        exif_dict["0th"][0x010e] = description
        exif_bytes = piexif.dump(exif_dict)
        image.save(path + "\\" + "tagged_" + fileName, "jpeg", exif=exif_bytes, quality="keep", optimize=True)
    os.rename(path + "\\" + fileName, path + "\\to_delete\\" + fileName)
