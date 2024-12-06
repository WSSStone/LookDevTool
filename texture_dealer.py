import os, sys
import cv2
import numpy as np
from console.utils import wait_key
from utils.path_helper import handle_spaced_dir

def texture_resize(srcdir:str, dstdir:str, name:str, size:int, interpolation:int=cv2.INTER_CUBIC) -> np.ndarray:
    srcpath = os.path.join(srcdir, name)
    dstpath = os.path.join(dstdir, name)

    ori = cv2.imread(srcpath)
    ori = cv2.resize(ori, (size, size), interpolation=interpolation)

    cv2.imwrite(dstpath, ori)

def texture_exchange_channel(path:str):
    img = cv2.imread(path)
    b, g, r = cv2.split(img)
    img = cv2.merge([r, g, b])
    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.imwrite(path, img)

def texture_concatenate(dir:str, rname:str, gname:str, bname:str) -> np.ndarray:
    rpath = os.path.join(dir, rname)
    gpath = os.path.join(dir, gname)
    bpath = os.path.join(dir, bname)
    respath = os.path.join(dir, "res.png")

    r = cv2.imread(rpath, cv2.IMREAD_GRAYSCALE)
    g = cv2.imread(gpath, cv2.IMREAD_GRAYSCALE)
    b = cv2.imread(bpath, cv2.IMREAD_GRAYSCALE)

    rgb = cv2.merge([b, g, r])
    cv2.imshow("rgb", rgb)
    cv2.waitKey(0)

    cv2.imwrite(respath, rgb)
    
    return rgb

def main(argv) -> None:
    if len(argv) < 3:
        print("Empty Input: operation, texture path, parameter")
        return
    
    if argv[1] == "resize":
        texture_resize(argv[2], argv[3], argv[4], int(argv[5]))

    if argv[1] == "concatenate":
        texture_concatenate(argv[2], argv[3], argv[4], argv[5])

    if argv[1] == "exchange":
        texture_exchange_channel(argv[2])

if __name__ == '__main__':
    main(sys.argv)