# Harris-Corner-Detector
Hi, reader! First of all, I know OpenCV already implemented harris corner. But I wanted to implement myself to understood the algorithm clearly.

Anyway, I want to explain my code and algorithm. Let's start!


Before start, I want to thanks Mr. Daniilidis from Penn University to explain this algorithm such a good way in Edx course. Also, my implemantation depends on these course.

The algorithm as like below,

```
#1 Read Input Image and convert grayscale
#2 Smooth input image with a Gaussian filter
#3 Create a gradient image
#4 Compute A, B and C matrix with Gaussian filter
#5 Compute corner response at each pixel 
    R = A*B-C*C*k*(A+B) where k is Harris Corner Free parameter
#6 Detect local maxima and minima of R whose value are above and below a threshold, respectively
```

### Step 1

```
im = cv2.imread("harris.jpg") 
im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) 
R = np.zeros(im_gray.shape) 
```
Image read by imread and converted. Also, dummy R 2d array created.

### Step 2

```
im_gray = cv2.GaussianBlur(im_gray,(5,5),1)
```
Applied Gaussian filter with 5x5 kernel and sigma is equal to 1.

### Step 3
```
Ix = cv2.Sobel(im_gray, cv2.CV_64F, 1, 0, ksize=5) 
Iy = cv2.Sobel(im_gray, cv2.CV_64F, 0, 1, ksize=5)
```

X and Y gradient created using Sobel filter. Again the sobel kernel is 5x5.

### Step 4
```
A = cv2.GaussianBlur(np.multiply(Ix, Ix),(5,5),1) 
B = cv2.GaussianBlur(np.multiply(Iy, Iy),(5,5),1)  
C = cv2.GaussianBlur(np.multiply(Ix,Iy),(5,5),1) 
```

A, B and C matrix created and applied a Gaussian filter.

### Step 5
```
k = 0.04
R = np.multiply(A,B)-np.square(C)-k*np.square(A+B)
```
R matrix calculated. These matrix is the corner response.

### Step 6
```
max_Val = 0.01*R.max()
for row_number,row in enumerate(R):
     for col_number,val in enumerate(row):
          if val > max_Val:  # Corner Detector
             im[row_number,col_number] = [0,0,255] 
          if val < -max_Val:  # Edge Detector
              im[row_number,col_number] = [0,255,0] 
          else: 
              pass
```

To detect the corner and edge, maximum value has been choosen as 1% of maximum value. If the value is bigger than threshold it is corner(red).
If it is lower than negative of threshold value, it is an edge(green). Otherwise, it is flat.

## Result
#### Input Image 
![alt text](https://raw.githubusercontent.com/mhepeyiler/Harris-Corner-Detector/master/harris.JPG)

#### Output Image 
![alt text](https://raw.githubusercontent.com/mhepeyiler/Harris-Corner-Detector/master/result.png)

## Reference

For further information, please read,
Harris, C. H. R. I. S., and M. I. K. E. Stephens. "A combined corner and edge detector. 1988." Cited on: 69.

Also you can check edx course,
https://www.edx.org/course/robotics-vision-intelligence-and-machine-learning
