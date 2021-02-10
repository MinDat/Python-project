#!/usr/bin/env python3

from PIL import Image
import os

def main():
    list_dir = os.listdir("images")
    for f in list_dir:
        if "ic" in f:
            im = Image.open("images/{}".format(f))
            im.resize((128,128)).rotate(90)

            

            im.save("mod/{}".format(f))

    # im = Image.open("images/ic_add_location_black_48dp")
    # new_im = im.resize((128,128)).rotate(90)
    # new_im.save("ic_add_location_black_128dp.ico")

main()
