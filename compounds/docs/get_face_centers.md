### ***get_face_centers***
When an object containing faces is connected to this compound, it will return the face center positions as a geo_property on the object, and a float3 array.  It will also return the face_indicies as a 2d uint array.  This compound only works on meshes.  If an object without faces is connected (points, strand etc) the object will pass through the compound unchanged.<br />

***
## Input
<span style="color:#90A3F4">***mesh_input***</span>
<br />The mesh to find the face centers on.

## Display Options
<span style="color:#E69963">***shape***</span>
<br />The shape of the face center display.

<span style="color:#82D99F">***default_size***</span>
<br />The size of the face center display.

<span style="color:#A8D977">***color***</span>
<br />The color of the face center display.

***
## Output
<span style="color:#90A3F4">***mesh_output***</span>
<br />The mesh, with the `face_center` geo property.

<span style="color:#A8D977">***face_centers***</span>
<br />The face_center data as a float3 array.

<span style="color:#62CFD9">***face_point_indicies***</span>
<br />A 2d array containing the index of each point making up each face.

