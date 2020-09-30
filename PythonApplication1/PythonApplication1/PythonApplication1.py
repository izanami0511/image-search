import cv2
import time
start_time = time.time()

#Загружаем изображения
img = cv2.imread("C:\main.jpg")
own = cv2.imread("C:\own.jpg")

#Отображение файла встроенными средствами OpenCV. 
def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main_programm(img,own):
   
    res = cv2.matchTemplate(img, temp, cv2.TM_CCORR_NORMED)
    _minVal, _maxVal, minLoc, maxLoc = cv2.minMaxLoc(res)
    matchLoc = maxLoc
    cv2.rectangle(img, matchLoc, (matchLoc[0] + temp.shape[0], matchLoc[1] + temp.shape[1]), (0,255,13), 3, 8, 0 )
    viewImage(resized_img, "Image-Main")
    
        

def main():
    main_programm(img,own)
    print("The work was done successfuly!")
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()