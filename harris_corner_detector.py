import cv2
import numpy as np

def main():

    #Step 1
    im = cv2.imread("harris.jpg") 
    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) 
    R = np.zeros(im_gray.shape) 

    #Step 2 
    im_gray = cv2.GaussianBlur(im_gray,(5,5),1)

    #Step 3
    Ix = cv2.Sobel(im_gray, cv2.CV_64F, 1, 0, ksize=5) 
    Iy = cv2.Sobel(im_gray, cv2.CV_64F, 0, 1, ksize=5)

    #Step 4 and 5
    A = cv2.GaussianBlur(np.multiply(Ix, Ix),(5,5),1) 
    B = cv2.GaussianBlur(np.multiply(Iy, Iy),(5,5),1)  
    C = cv2.GaussianBlur(np.multiply(Ix,Iy),(5,5),1)   

    #Step 6
    k = 0.04
    R = np.multiply(A,B)-np.square(C)-k*np.square(A+B)

    #Step 7 and 8
    max_Val = 0.01*R.max()
    for row_number,row in enumerate(R):
        for col_number,val in enumerate(row):
            if val > max_Val:  # Corner Detector
                im[row_number,col_number] = [0,0,255] 
            if val < -max_Val:  # Edge Detector
                im[row_number,col_number] = [0,255,0] 
            else: 
                pass

    cv2.imshow("Detected", im)
    if cv2.waitKey(0) & 0xFF ==27:
        cv2.destroyAllWindows()
            
if __name__ == "__main__":
    main()