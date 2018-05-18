#-*- coding:utf-8 -*-
import cv2
from pathlib import Path

def rgb_to_gray(src):
    r, g, b = src[:,:,0], src[:,:,1], src[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray   
    
def main():
    src_path = Path('src')
    for path in src_path.iterdir():
        img = cv2.imread('src/' + path.name)
        gray_img = rgb_to_gray(img)
        cv2.imwrite('dist/' + path.name, gray_img)

if __name__ == "__main__":
    main()