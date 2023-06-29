### ***strand_to_mesh***
Converts a strand to a mesh using tube or ribbon extrusion. It takes into account the `point_size` property for the thinkness of the extrusions, and allows you to set a base, minimum and maximum width.<br />Uses compounds from both Maxime Jeanmougin and Aslan Jafari with all thanks and credit to them.<br />

***
## Input
<span style="color:#90A3F4">***incoming_strand***</span>
<br />The strand to be converted to a mesh.

<span style="color:#62CFD9">***extrusion_shape***</span>
<br />The shape of the extrusion.  Tube is good for wires and cables, ribbon is more suited to roads and streamers.

<span style="color:#82D99F">***base_width***</span>
<br />The base width of the output mesh, based on `point_size` property.

<span style="color:#82D99F">***minimum_width***</span>
<br />The minimum width of the extrusion.

<span style="color:#82D99F">***maximum_width***</span>
<br />The maximum width of the extrusion.

#### Ribbon Settings
<span style="color:#62CFD9">***axis***</span>
<br />Which axis to extrude the ribbon along.  Strand normal, strand binormal or custom.

<span style="color:#A8D977">***custom_axis***</span>
<br />The custom axis for extrusion.

#### Tube Settings
<span style="color:#62CFD9">***tube_sides***</span>
<br />Number of sides in the resulting tube.

<span style="color:#E69963">***start_cap***</span>
<br />Apply a start cap to the tube extrusion.

<span style="color:#E69963">***end_cap***</span>
<br />Apply an end cap to the tube extrusion..

***
## Output
<span style="color:#82D99F">***mesh_output***</span>
<br />The resulting mesh.

