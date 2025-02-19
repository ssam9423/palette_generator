"""Color Palette Generator From Image - Samantha Song - started 2025.01.31"""
# Take in Image
# Sort Colors in Image by Appearance
# Determine Colors that are "Distinct"
# Determine Colors that have good color contrast

import sys
from PIL import Image
import numpy as np

# File name and path
FILE_NAME = 'example.png'
IMG_PATH = 'Images'

# Command Line - Args
args = sys.argv
if len(args) == 2:
    FILE_NAME = args[1]
    IMG_PATH = ''
elif len(args) == 3:
    FILE_NAME = args[2]
    IMG_PATH = args[1]

try:
    # Open file and convert into list of pixels
    img = Image.open(f"{IMG_PATH}\\{FILE_NAME}")
    img_np = np.array(img)
    pixels = np.array(img).reshape(-1, 3)

    # Get unique pixel colors and counts and sort by largest number of counts
    unique_ci, counts = np.unique(pixels, return_counts=True, axis=0)
    color_counts = np.column_stack((unique_ci, counts))
    color_counts = sorted(color_counts, key=lambda x: x[3])[::-1]

    # Determine Color Palette
    palette = np.empty((0,3), int)
    NUM_COLORS = 5      # Maximum number of colors in palette
    color_ind = 0       # Color Index for color_counts
    DIFFERENCE = 30     # Differece in rgb values from rest of palette

    # While there are still individual colors to iterate through
    while color_ind < len(color_counts):
        # If palette is complete
        if len(palette) >= NUM_COLORS:
            break
        # Determines first color in palette
        elif len(palette) == 0:
            new_color = color_counts[color_ind][0:3]
            palette = np.vstack((palette, new_color))
        # Determines if color gets added to palette
        else:
            new_color = color_counts[color_ind][0:3]
            is_diff = True
            # Determines if color is distinct enough from rest of palette
            for i, color in enumerate(palette):
                for rgb in range(3):
                    if abs(new_color[rgb]-palette[i][rgb]) < DIFFERENCE:
                        is_diff = False
            # If color is distinct from rest of palette, add color to palette
            if is_diff:
                palette = np.vstack((palette, new_color))
        color_ind += 1

    # Add palette colors to bottom of image
    img_w = img_np.shape[1]
    img_h = img_np.shape[0]
    palette_w = int(img_w/(palette.shape[0]))
    PALETTE_H = 10

    # Add palette pixels to image
    for h_pixel in range(PALETTE_H):
        for w_pixel in range(img_w):
            # Determine which color from palette to add to image
            palette_ind = int(w_pixel/palette_w)
            # Make sure palette_ind is within range
            if palette_ind >= len(palette):
                palette_ind = len(palette) - 1
            palette_color = palette[palette_ind]
            pixels = np.vstack((pixels, palette_color))

    # Shape of image with palette at bottom
    new_img_shape = (img_h+PALETTE_H, img_w, 3)

    # Reshape back to the original image dimensions
    palette_img_np = np.array(pixels).reshape(new_img_shape)
    palette_img_np = palette_img_np.astype(np.uint8)

    # Convert back to PIL Image
    palette_img = Image.fromarray(palette_img_np)
    palette_img.show()

    NEW_FILE_NAME = 'palette_' + FILE_NAME
    palette_img.save(f'{IMG_PATH}\\{NEW_FILE_NAME}')
except FileNotFoundError:
    print('The format should be:')
    print('python palette_generator.py <image file>')
    print('or')
    print('python palette_generator.py <image path> <image file>')
