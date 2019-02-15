import os
import utils
import single

extensions = ['jpg', 'jpeg', 'png', 'ico', 'bmp', 'tiff', 'pnm']

def batch_convert(input_path, specific_format, output_path, format):
    failed = 0
    succeeded = 0
    images = utils.System.files_tree_list(input_path, extensions=[specific_format])
    print("~ Total found images: {}".format(len(images)))
    image_name = ''
    for image in images:
        if image.count("/") > 0 and not image.count("\\") > 0:
            image_name = image.split(r".")[0].split("/")[-1]

        else:
            image_name = image.split(r".")[0].split("\\")[-1]
        try:
            single.single_convert(image, output_path + os.sep + image_name, format)
        except:
            print("- Failed to convert {}".format(image))
            failed += 1


if __name__ == "__main__":
    batch_convert("images", "jpg", "output", "png")
