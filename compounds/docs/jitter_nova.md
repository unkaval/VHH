### ***jitter_nova***
New version of the ancient jitter node.  Randomly moves points around on strands, meshes and pointclouds<br />

***
## Input
<span style="color:#90A3F4">***in_geo***</span>
<br />The object you wish to jitter.

<span style="color:#82D99F">***magnitude***</span>
<br />The magnitude of the jitter.

<span style="color:#82D99F">***frequency***</span>
<br />The frequency of the jitter.

<span style="color:#62CFD9">***seed***</span>
<br />The seed of the jitter.

<span style="color:#A8D977">***jitter_axis***</span>
<br />Axis along which to jitter.

<span style="color:#E69963">***jitter_along_normal***</span>
<br />Disables jitter axis and jitters along the normals if the `point_normal` property exists.

<span style="color:#E69963">***update_mesh_normals***</span>
<br />If your input is a mesh, update it's normals before output.


***
## Output
<span style="color:#90A3F4">***output***</span>
<br />The jittered object.

