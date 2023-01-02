### ***update_point_curvature***
High level node including `point_curvature`.  Please see the Info tab of that node for more detail.<br />

***
## Input
<span style="color:#90A3F4">***in_geo***</span>
<br />Input geometry.

<span style="color:#82D99F">***curvature_scale***</span>
<br />The scale of the edge lengths.  This can affect the final output.

<span style="color:#82D99F">***curvature_radius***</span>
<br />When a point cloud, or abject without connectivity is connected, this is the radius by which the neighbors are calculated.

<span style="color:#CCB699">***adjust_curvature***</span>
<br />An fCurve property allowing adjustment of the output.

***
## Output
<span style="color:#82D99F">***geometry_with_curvature***</span>
<br />Input geometry with the curvature property included.

<span style="color:#82D99F">***property***</span>
<br />The name of the curvature property used (set internally).

