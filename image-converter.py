
import argparse
import re, os, sys
sys.path.append("core/")

import single
import batch


description = """
This is command line utility used for converting image format to any other available 
image formats.

Basic usage:
> image-converter.exe -i INPUT -o OUTPUT 
or
> image-converter.exe --input INPUT --ouput OUTPUT

"""
output_help = "supply image name & ext for single image. for batch images supply output path only"
input_help  = "supply image name & ext for single image. for batch images supply input path only"

argument_parser= argparse.ArgumentParser(prog="image-converter",
                                         description=description, 
                                         formatter_class=argparse.RawDescriptionHelpFormatter
                                         )
argument_parser.add_argument("-i", "--input", required=True, help=input_help)
argument_parser.add_argument("-o", "--output", required=True, help=output_help)
argument_parser.add_argument("-b", "--batch", action='store_true', help="path to images folder")
argument_parser.add_argument("-f", "--format", help="output extension: used with -b e.g: jpg, png, ...")
argument_parser.add_argument("-s", "--specific", help="convert specific format from folder")

args = vars(argument_parser.parse_args())

# single image
if not args["batch"]:
    print("* Converting single image")
    single.single_convert(args["input"], args["output"])

# batch images    
elif args["batch"]:
    print("* Converting batch images")  
    if os.path.exists(args["input"]):
        if not os.path.exists(args["output"]): os.mkdir(args["output"]); print("* Creating output folder")
        batch.batch_convert(args["input"], args["specific"], args["output"], args["format"])        
    else:
        print("- Input path does not exist!")
