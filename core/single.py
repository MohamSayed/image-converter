import PIL.Image as Image
import re
import sys
import os


def single_convert(in_path, out_path, extension=''):
    if not extension:
        extension = re.findall(r"\.\w*", out_path)[0][1:]
    if os.path.exists(in_path):
        image = Image.open(in_path)
        try:
            image.save(out_path + '.' + extension)
            image.close()
            print("~ Converting: {} > {} ".format(in_path, extension))

        except Exception as e:
            print("{} : error in single image: {}".format(e, in_path))

    else:
        print("Input file or path doesn't exist!")
        sys.exit()


if __name__ == "__main__":
    single_convert("beautiful.jpg", "converted_beautiful.png")
