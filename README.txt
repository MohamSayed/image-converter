# Image-converter version 0.2

This is a python tools used for converting image formats to other formats

Basic usage: 
image-converter.py -i INPUT -o OUTPUT
or 
image-converter.py --input INPUT --ouput OUTPUT



Single image example:
> image-converter.py -i input_image.jpg -o output_image.png

Batch images example:
> image-converter.py -b -e png -i input_folder -o output_folder

-b: enable batch 
-e or --ext: new extension

Get help:
> image-converter.py -h

Here, I changed the format of the image from 'png' to 'jpg'.



