### ***extrude_and_average***
Taking in an array of meshes, this compound will use the `extrude` and `median_property_blur` compounds.  Extruding and averaging the verticies of the incoming array.  Note: this compound is auto-looped, so while the `mesh_array` input looks like a single mesh input, it wants an array.<br />

***
## Input
<span style="color:#90A3F4">***mesh_array***</span>
<br />Incoming mesh array.

<span style="color:#62CFD9">***blur_amount***</span>
<br />How much you want to average the verticies.

<span style="color:#82D99F">***extrusion_thickness***</span>
<br />How thick the extrustion should be.

***
## Output
<span style="color:#90A3F4">***out_mesh***</span>
<br />The resulting mesh array.

