import PIL.Image as Image
import re, sys, os

def single_convert(in_path, out_path, extension=''):
    if not extension: extension = re.findall(r"\.\w*", out_path)[0][1:]
    if os.path.exists(in_path):
        image = Image.open(in_path)
        image.save(out_path + '.' + extension)
        print("~ Converting: {} > {} ".format(in_path, extension))
 
    else:
        print("Input file or path doesn't exist!")
        sys.exit()



if __name__ == "__main__":
    single_convert("beautiful.jpg", "converted_beautiful.png")