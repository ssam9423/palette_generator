# Color Palette Generator
## Description
This program generates a color palette based on an image.
It then saves a new image which is the original image with a bar at the bottom displaying the color palette.

<p align="center">
    <div class="row">
        <img src="/example.png" width="300" height="200"/>
        <img src="/palette_example.png" width="300" height="200"/>
    </div>
</p>
<p align="center">
    <div class="row">
        <img src="/leaves.jpg" width="300" height="200"/>
        <img src="/palette_leaves.jpg" width="300" height="200"/>
    </div>
</p>

## Adapting the Code
Update the `FILE_NAME` to the name of the image that the color palette will be based on. 
The image with the color palette will be saved as a new image with the file name 'palette' + `FILE_NAME`.

`NUM_COLORS` is the maximum number of colors that will be generated in the color palette. By default, this is set to 5. 
In the event that the image does not have distinct enough colors, the number of colors in the color palette will be less than `NUM_COLORS`.

`DIFFERENCE` represents the threshold that a new color needs to pass in order to be added to the color palette.
This was added to ensure that the colors in the color palette are distinct.
Each RGB value of each color in the color palette needs to be at least +/- the `DIFFERENCE` from the other colors in the generated color palette.

For more distinct colors, the `DIFFERENCE` can be increased, however this will potentially result in less colors in the color palette.
To generate more colors in the color palette, the `DIFFERENCE` may need to be decreased, however this may result in less distinct colors.

```
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
```

## Example Images
Some examples of what this program does are also in this repository.
For both examples, the `NUM_COLORS` was set to 5.
> [!NOTE]
> Although NUM_COLORS` was set to 5 for both images, palette_leaves.jpg only has 4 colors in its color palette.
> This is because the colors in the original image leaves.jpg were not distinct enough.

