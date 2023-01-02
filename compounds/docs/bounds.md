### ***bounds***
Generates and returns a bounding object for a geometry.<br />

***
## Input
<span style="color:#90A3F4">***in_mesh***</span>
<br />The mesh to have its bounds returned.

<span style="color:#62CFD9">***bounds_type***</span>
<br />What to you wish returned, options are *cube, xz plane, yz plane, xy plane* and *sphere*.

<span style="color:#A8D977">***offset_bounds***</span>
<br />An offset you can add to the bounds.

<span style="color:#A8D977">***padding***</span>
<br />Extra distance to add to the bounds in 3 dimensions.

<span style="color:#82D99F">***sphere_padding***</span>
<br />Extra distance to add to the bounding sphere.

***
## Output
<span style="color:#90A3F4">***out_mesh***</span>
<br />If the `bounds_type` **is not** set to `sphere`, the outgoing mesh with `min_bound` and `max_bound` set as **properties**.  

<span style="color:#90A3F4">***out_bounds***</span>
<br />The bounding geometry.


