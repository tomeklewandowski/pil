from PIL import Image
import glob, os
from config import *

class Editor:

    def __init__(self):
        # setting default value
        self.conf = Config()

    def set_config(self,conf):
        self.conf = conf

    def run(self):
        for infile in glob.glob("media/*.jpg"):
            self.edit(infile)

    def edit(self, infile):
        file, ext = os.path.splitext(infile)
        im = Image.open(infile)
        im = self.act_edit(im)
        im.save(file + ".edited", "JPEG")

    def act_edit(self, im):
        if self.conf.ROTATE != None:
            im = im.rotate(self.conf.ROTATE)
        if self.conf.IMAGE_W != None or self.conf.IMAGE_H != None:
            im = im.resize((self.conf.IMAGE_W, self.conf.IMAGE_H))
        if self.conf.WHITE_BLACK != None:
            im = im.convert("L")
        return im