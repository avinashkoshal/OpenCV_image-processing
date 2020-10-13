# Color Filtering
- In order to perform the color filtering we first need to understand the HSV color space

## How it works
 1) Convert the BGR color space of image to HSV color space 
 2) Choose threshold of Specific color in HSV space 
 3) Prepare the mask to overlay 
 4) Do a bitwise_AND

The black region in the mask has the value of 0, 
so when multiplied with original image removes all non-saffron regions 

## TO run the code
 - Place your desired image in Images folder and specify its path in main file
 - Python3 color_filter.py