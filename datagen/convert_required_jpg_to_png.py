import numpy as np
import cv2 as cv
import os

if __name__ == "__main__":

    required_images_file_path = "./cocopng.txt"
    jpg_path = "/home/burak/coco_dataset/unlabeled2017/"
    png_path = "/home/burak/coco_dataset/unlabeled2017_png/"

    with open(required_images_file_path) as fp:
        lines = fp.readlines()
        for line in lines:
            long_file_str = line.split()[0]
            filename = long_file_str.split('/')[-1]
            basename = filename.split('.')[0]
            img_jpg = os.path.join(jpg_path, basename+".jpg")
            img_png = os.path.join(png_path, basename+".png")
            if os.isfile(img_png):
                print("Skipping image since {} already exists.".format(img_png))
                continue
            img = cv.imread(img_jpg, cv.IMREAD_COLOR)
            b_channel, g_channel, r_channel = cv.split(img)
            alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 255
            alpha_channel[0, 0] = 254
            img_BGRA = cv.merge((b_channel, g_channel, r_channel, alpha_channel))
            print("Converting {} to {}, size={}".format(img_jpg, img_png, img_BGRA.shape))
            cv.imwrite(img_png, img_BGRA)


