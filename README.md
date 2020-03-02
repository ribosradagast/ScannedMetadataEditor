# ScannedMetadataEditor
Simple script for helping to tag Grandma G's photo scans


To run:
```
python GenerateIndex.py C:\Users\justi\Pictures\FastFoto\1989_April
```

Which generates a list of the files in that directory, as well as slots for description and date taken

Then run 
```
python IndexProcessor.py C:\Users\justi\Pictures\FastFoto\1989_April
```

to read the index out of that directory, apply the supplied description and date taken, and then rename and "delete" the old files
