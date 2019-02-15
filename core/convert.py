from PyQt5.QtCore import QThreadPool, QObject, QRunnable, pyqtSignal, QThread

import single

import os


class Worker(QRunnable):
    def __init__(self, progressbar, images, output_image_path, extension):
        super(Worker, self).__init__()
        self.progressbar = progressbar
        self.output_image_path = output_image_path
        self.extension = extension
        self.images = images

    def run(self):
        self.convert_and_save()

    def convert_and_save(self):
        self.progressbar.setValue(0)

        # warning: hardcoded
        _progress = 1
        self.progressbar.setMaximum(len(self.images))
        if self.output_image_path and self.images:
            for image in set(self.images):
                self.progressbar.setValue(_progress)
                _progress += 1
                image_name = ''
                if image.count("/") > 0 and not image.count("\\") > 0:
                    image_name = image.split(r".")[0].split("/")[-1]

                else:
                    image_name = image.split(r".")[0].split("\\")[-1]

                final_outpath = self.output_image_path + os.sep + image_name

                single.single_convert(
                    image, self.output_image_path, extension=self.extension)
