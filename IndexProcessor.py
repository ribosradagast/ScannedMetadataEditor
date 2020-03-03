import os
import sys

from pyexiv2 import Image

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

path = sys.argv[1]
entries = os.scandir(path)

indexFile = open(path + "\\index.txt", mode="r", encoding="utf-8")
os.mkdir(path + "\\to_delete\\")

next_date_for_pictures = ''
num_photos_with_date = 0

while True:
    fileName = indexFile.readline().strip()
    description = indexFile.readline().strip()
    dateTaken = indexFile.readline().strip()
    if not dateTaken: break  # EOF

    if description != 'delete':
        metadata = Image(path + "\\" + fileName)
        xmp = {'Xmp.dc.description': description}
        metadata.modify_xmp(xmp)

        if dateTaken == next_date_for_pictures:
            # add a second to make the next picture think that it comes next
            split_date = dateTaken.split(":")
            minutes = split_date[3]
            split_date[3] = str(int(minutes) + num_photos_with_date).zfill(2)
            num_photos_with_date += 1
            dateTaken = ":".join(split_date)
        else:
            num_photos_with_date = 1
            next_date_for_pictures = dateTaken

        exif = {
            'Exif.Image.ImageDescription': description,
            'Exif.Photo.DateTimeOriginal': dateTaken
        }
        metadata.modify_exif(exif)
        metadata.close()
    else:
        os.rename(path + "\\" + fileName, path + "\\to_delete\\" + fileName)
