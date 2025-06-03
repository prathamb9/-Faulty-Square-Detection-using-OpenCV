'''
*********************************************************************************
*
*        		===============================================
*           		        CYBORG OPENCV TASK 2
*        		===============================================
*
*
*********************************************************************************
'''

# Author Name:		Pratham Borgaonkar
# Roll No:			124CS0126
# Filename:			task_2A_Pratham.py
# Functions:		detect_faulty_squares


####################### IMPORT MODULES #######################
import cv2
import numpy as np
##############################################################


def detect_faulty_squares(image):
    faulty_squares = {}
    color_names = {
        (0, 165, 255): 'Orange',
        (0, 255, 0): 'Green',
        (255, 255, 0): 'Blue',
        (0, 0, 255): 'Red'
    }

    black_pixel = [0, 0, 0]
    white_pixel = [255, 255, 255]
    start_x, start_y = 105, 105
    step = 60

    for row in range(8):
        for col in range(8):
            label = f"{chr(65 + row)}{col + 1}"
            pixel_color = image[start_y, start_x]

            should_be_black = (row + col) % 2 != 0
            if should_be_black:
                if not np.allclose(pixel_color, black_pixel):
                    key = (color_names.get(tuple(pixel_color), "Unknown"), label)
                    faulty_squares[key] = "Black"
            else:
                if not np.allclose(pixel_color, white_pixel):
                    key = (color_names.get(tuple(pixel_color), "Unknown"), label)
                    faulty_squares[key] = "White"

            start_x += step

        start_y += step
        start_x = 105

    return faulty_squares