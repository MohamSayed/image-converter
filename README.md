# image-converter

v0.3
[Release](https://sourceforge.net/projects/image-converter-cmd)

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
-s or --specific: convert only specifc format  

Get help:
> $ python image-converter.py -h

Here, I changed the format of the image from 'png' to 'jpg'.

# Features
* batch converting
* Simple User Intefrace

# Donate PayPal:
* https://www.paypal.me/eagle6789
* me49544@gmail.com

# Donate BTC:
* 1AP6bypSaFt7ptFydmjuWWWS8a9MCWRt3m

# Contact me :
* me.dev67894@gmail.com

