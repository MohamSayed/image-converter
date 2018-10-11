import os
import utils
import single

extensions = ['jpg', 'jpeg', 'png', 'ico', 'bmp', 'tiff', 'pnm']

def batch_convert(path, to, extension):
    failed = 0
    succeeded = 0
    counter = 0
    images = utils.System.files_tree_list(path, extensions=extensions)
    print("~ Total found images: {}".format(len(images)))
    
    for image in images:
        try:
            single.single_convert(image, to + os.sep + str(counter) + '.' + extension, extension)
            counter+=1
        except:
            print("- Failed to convert {}".format(image))
            failed += 1


if __name__ == "__main__":
    batch_convert("images", "test/", "png")