### ***quick_grid***
Quick point grid generator.
<br /><br />[<span style="color:#CCB699">**quick_grid (youtube)**</span>](https://youtu.be/M8I1YzLDlds)

***
## Input
<span style="color:#62CFD9">***x|y|z***</span>
<br />The number of points in x|y|z.

<span style="color:#82D99F">***x_step|y_step|z_step***</span>
<br />The distance between the points in x|y|z.

<span style="color:#A8D977">***offset***</span>
<br />An offset for the entire grid.   

<span style="color:#E69963">***honeycomb***</span>
<br />Offsets the points in the x direction by half the x step.

<span style="color:#82D99F">***point_size***</span>
<br />The point size for display. 

<span style="color:#E69963">***centered***</span>
<br />Moves the entire grid to be centered on the origin.

<span style="color:#A8D977">***default_color***</span>
<br />A single color value to apply to all the points.  

<span style="color:#E69963">***show_zero***</span>
<br />Inverts the colour of the first point in the array.

<span style="color:#A8D977">***color_in***</span>
<br />An array of color values to apply to the points.  Best results from the same size as the number of points in the grid.   

***
## Output
<span style="color:#A8D977">***grid_positions***</span>
<br />A float3 array containing the positions of the points. 

<span style="color:#90A3F4">***points***</span>
<br />A points object output.  

<span style="color:#62CFD9">***number_of_points***</span>
<br />Number of points in the resulting grid.



