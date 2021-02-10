#!/usr/bin/env python3

from PIL import Image
import os

def main():
    # List all files in images
    list_dir = os.listdir("images")
    for f in list_dir:
        # looking for file that start with ic_
        if f.startswith("ic_"):
            # open file image in images dir as object
            im = Image.open("images/{}".format(f))
            # rotate
            im.rotate(270)
            #resize
            im.resize((128,128))
            # save in the diference dir name mod
            im.save("mod/{}.ico".format(f))

main()
