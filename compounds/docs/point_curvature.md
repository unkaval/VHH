### ***point_curvature***
Calculates a [point_curvature] property based on the average of all connected edges and point normal.  Also works on objects without connectivity (point clouds) by generating normals from the centroid of the object and making vectors between neighbors.  This compound will attempt to generate normals if none exist.<br />

***
## Input
<span style="color:#90A3F4">***in_geo***</span>
<br />The geometry input.  Supports meshes and point objects.

<span style="color:#82D99F">***scale***</span>
<br />The scale of the edge lengths.  This can affect the final output.

<span style="color:#82D99F">***radius***</span>
<br />When a point cloud, or abject without connectivity is connected, this is the radius by which the neighbors are calculated.

<span style="color:#CCB699">***adjust_curvature***</span>
<br />An fCurve allowing you to adjust the curvature.

***
## Output
<span style="color:#90A3F4">***out_geo***</span>
<br />The input object with the [point_curvature] property.

<span style="color:#82D99F">***adjusted_curvature***</span>
<br />The curvature data, mapped to the adjustment curve.

<span style="color:#82D99F">***raw_curvature***</span>
<br />The raw curvature data.