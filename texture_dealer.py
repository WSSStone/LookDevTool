import os, sys
import cv2
import numpy as np
from console.utils import wait_key
from utils.path_helper import handle_spaced_dir

def texture_resize(path:str, size:int, interpolation:int=cv2.INTER_CUBIC) -> np.ndarray:
    ori = cv2.imread(path)
    ori = cv2.resize(ori, (size, size), interpolation=interpolation)
    
    cv2.imshow("", ori)
    cv2.waitKey(0)

    cv2.imwrite(path, ori)

def main(argv) -> None:
    if len(argv) < 4:
        print("Empty Input: texture path, operation, parameter")
        return
    
    fpath = handle_spaced_dir(argv[:-2:])
    
    if argv[-2] == "resize":
        texture_resize(fpath, int(argv[-1]))

if __name__ == '__main__':
    main(sys.argv)