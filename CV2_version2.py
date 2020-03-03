import numpy as np
import cv2
import argparse
from threading import Thread
import random

def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(name_of_window, cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def cropImage(image, x_start,x_end,y_start,y_end,Text):
    weight = image.shape[1]
    height = image.shape[0]
    crop = image[x_start:x_end, y_start:y_end] #[y:y+height, x:x+weight]
    viewImage(crop, "Cropped")
    weight_cr = crop.shape[1]
    height_cr = crop.shape[0]
    y = random.randint(50,height_cr-50)
    x = random.randint(1,weight_cr)
    output = crop.copy()
    cv2.putText(output, "{}".format(Text),(x,y),cv2.FONT_HERSHEY_SIMPLEX,2,(20 ,30 ,40),2)
    viewImage(output,"Test")
    print(x,y)
def RandomcropImage(image,Text):
    weight = image.shape[0]
    height = image.shape[1]
    x_start = random.randint(1,weight/2)
    x_end = random.randint(x_start,weight)
    y_start = random.randint(1,height/2)
    y_end = random.randint(y_start,height)
    crop = image[x_start:x_end, y_start:y_end] #[y:y+height, x:x+weight]
    viewImage(crop, "Cropped")
    weight_cr = crop.shape[1]
    height_cr = crop.shape[0]
    y = random.randint(50,height_cr/2)
    x = random.randint(1,weight_cr/2)
    output = crop.copy()
    cv2.putText(output, "{}".format(Text),(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(255 ,47 ,40),1)
    viewImage(output,"Test")
    print(height_cr, weight_cr, x, y)
    print(x_start, x_end, y_start, y_end)

#/home/xyqer/Desktop/Python/wallpaper.jpg
random.seed()
parser = argparse.ArgumentParser()
parser.add_argument('--path')
d_parser = parser.add_mutually_exclusive_group()
d_parser.add_argument('--show', action='store_const', const=True, default=False)
d_parser.add_argument('--crop', nargs='+', default=[''])
args = parser.parse_args()
image = cv2.imread("{}".format(args.path))
Temp = np.array(args.crop)
Temp_1 = Temp.shape[0]
Text = ""
i = 4
if args.show:
    viewImage(image,"Test")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif args.crop:
    if Temp.shape[0] > 1:
        x_start = int(args.crop[0])
        x_end = int(args.crop[1])
        y_start = int(args.crop[2])
        y_end = int(args.crop[3])
        while Temp_1 > i:
            Text += args.crop[i]
            Text += " "
            i += 1
        Thread(target = cropImage(image, x_start,x_end,y_start,y_end,Text)).start()
        Thread(target = viewImage(image, "Test")).start()
    else:
        Text = args.crop
        Thread(target = RandomcropImage(image,Text)).start()
        Thread(target = viewImage(image, "Test")).start()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
