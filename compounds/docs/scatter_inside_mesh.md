### ***scatter_inside_mesh***
Randomly scatter points inside a mesh object.  The compound checks to see if the incoming object is a mesh, and if it isn't, performs a passthrough.<br />

***
## Input
<span style="color:#90A3F4">***object_in***</span>
<br />Mesh to scatter inside.

<span style="color:#62CFD9">***number_of_points***</span>
<br />The number of points to randomly scatter.

<span style="color:#82D99F">***cull_in_radius***</span>
<br />When this is above zero, points within that radius will be culled.  Zero culls no points.

***
## Output
<span style="color:#82D99F">***positions***</span>
<br />scattered positions.

<span style="color:#90A3F4">***points***</span>
<br />Scattered points.

