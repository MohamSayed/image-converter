# image-converter

v 0.2

This is a python tool used for converting image formats to other formats, such as
jpg, png, tiff, ...

Basic usage: 
python image-converter.py -i INPUT -o OUTPUT
or 
python image-converter.py --input INPUT --ouput OUTPUT



Single image example:
> $ python image-converter.py -i input_image.jpg -o output_image.png

Batch images example:
> $ python image-converter.py -b -e png -i input_folder -o output_folder

> $ python image-converter.py -b -e png -i input_folder -o output_folder -s jpg

-b: enable batch 
-e or --ext: new extension
-s or --specific: convert only specifci format

Get help:
> $ python image-converter.py -h

Here, I changed the format of the image from 'png' to 'jpg'.

# Features
* batch converting

