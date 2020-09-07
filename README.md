# spaTab


```Python
use:
python3 -m spatab [--options] filename
```
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Options](#options)
* [Testing](#Testing)
* [Author](#author)

## General info

This program get a file and change spaces to tabs or tabs to spaces in the start of lines.
The file have to in the same folder that program.
You have to use program from place where pragram is located

## Technologies

Project is created with:
* Python 3

## Options

parameters:

    -f (--from) what kind of characters convert start, „tabs” or  „spaces”

    -r (--replace) – flag, if exist program don't copy file

    -t (--tab-chars) default 4, optional parameter how many spaces have one tab


    if user don't give -f parameter, program will do „guess” - spaces or tabs and return message
    
    
## Testing

If you want test code you have to install pytest

Run test:
```Python
python3 -m pytest
```

## Author

Przemyslaw Kula
https://github.com/pkula