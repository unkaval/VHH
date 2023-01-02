### ***update_point_density***
Local point density property generated based on number of point neighbors within a radius.<br />

***
## Input
<span style="color:#90A3F4">***mesh***</span>
<br />Input mesh.

<span style="color:#82D99F">***radius***</span>
<br />The radius per point used to calculate the density of the points.

<span style="color:#62CFD9">***number_of_neighbors***</span>
<br />The number of neighbors per point to include in the density calculations.

***
## Output
<span style="color:#82D99F">***out_geometry***</span>
<br />Output geometry with `point_density` and `normalized_point_density` carried as properties.

<span style="color:#82D99F">***point_density***</span>
<br />The point density property.

<span style="color:#82D99F">***normalized_point_density***</span>
<br />The point density property, scaled to a 0-1 range.

