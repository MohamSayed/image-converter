import os
import utils
import single

extensions = ['jpg', 'jpeg', 'png', 'ico', 'bmp', 'tiff', 'pnm']

def batch_convert(input_path, specific_format, output_path, format):
    failed = 0
    succeeded = 0
    counter = 0
    images = utils.System.files_tree_list(input_path, extensions=[specific_format])
    print("~ Total found images: {}".format(len(images)))
    
    for image in images:
        try:
            single.single_convert(image, output_path + os.sep + str(counter) + '.' + format, format)
            counter+=1
        except:
            print("- Failed to convert {}".format(image))
            failed += 1


if __name__ == "__main__":
    batch_convert("images", "jpg", "output", "png")
