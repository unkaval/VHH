### ***point_curvature***
Calculates a [point_curvature] property based on the average of all connected edges and point normal.  Also works on objects without connectivity (point clouds) by generating normals from the centroid of the object and making vectors between neighbors.  Without a valid normal, this **will not work**<br />

***
## Input
<span style="color:#90A3F4">***in_geo***</span>
<br />The geometry input.  Supports meshes and point objects.

<span style="color:#E69963">***normalized***</span>
<br />When on, normalizes the output between 0 and 1.  Because the curvature can be large, this is on by default.

<span style="color:#82D99F">***scale***</span>
<br />The scale of the edge lengths.  This can affect the final output when [normalized] is off.

<span style="color:#82D99F">***radius***</span>
<br />When a point cloud is connected, this is the radius by which the neighbors are calculated.

<span style="color:#E69963">***remap***</span>
<br />Remap the values.

<span style="color:#82D99F">***min***</span>
<br />Minimum remap value.

<span style="color:#82D99F">***max***</span>
<br />Maximum remap value.

***
## Output
<span style="color:#90A3F4">***out_geo***</span>
<br />The input object with the [point_curvature] property.

<span style="color:#82D99F">***curvature***</span>
<br />The curvature data.

