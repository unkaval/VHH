### ***displacer***
<font size = 1>**Component Compound** - this compound is a component in the the *displacer* ecosystem.<br /><br /></font>
<font size = 2>**displacer** - This is the main control compound for the displacer system.<br /><br />The **Diagnostic** tab on this node will display the low-res representation of your heightfield.<br />The **Final** tab is for rendering the higher-res in Arnold. This is setup internally for you, and will use an internal shader if none is plugged in.</font><br />

***
## Input
<span style="color:#90A3F4">***custom_object***</span>
<br />Simply, the object you wish to displace.  If this is empty, the compound assumes you are using the internal polygon plane.

<span style="color:#CCB699">***noise_2d***</span>
<br />Inputs for the scalar fields, you can right-click on the port to add some preset fields, or connect a scalar field here.

<span style="color:#CCB699">***noise_3d***</span>
<br />Inputs for the vector fields, you can right-click on the port to add some preset fields, or connect a vector field here.

<span style="color:#CCB699">***adjust_field***</span>
<br />An adjustment curve for the weights **output** field.

<span style="color:#82D99F">***ground_plane_length***</span>
<br />Length of the internal ground plane, in Maya units.

<span style="color:#82D99F">***ground_plane_width***</span>
<br />Width of the internal ground plane, in Maya units.

<span style="color:#62CFD9">***display_resolution_length***</span>
<br />This is the resolution of the display plane.  It's how many verticies along its length.

<span style="color:#62CFD9">***display_resolution_width***</span>
<br />This is the resolution of the display plane.  It's how many verticies along its width.

<span style="color:#62CFD9">***render_resolution_length***</span>
<br />This is the resolution of the render plane.  It's how many verticies along its length.

<span style="color:#62CFD9">***render_resolution_width***</span>
<br />This is the resolution of the render plane.  It's how many verticies along its width.

<span style="color:#90A3F4">***mask_by_object***</span>
<br />Inputs for any objects you wish to mask the incoming fields with.

<span style="color:#90A3F4">***mask_by_strand***</span>
<br />Inputs for any strands you wish to mask the incoming fields with.

<span style="color:#82D99F">***strand_radius***</span>
<br />If you are masking by a strand, this is how far away from the strand you wish to mask the fields.

<span style="color:#CCB699">***object_mask_falloff***</span>
<br />An fCurve controlling the falloff of the mask from the edge of the object.

<span style="color:#CCB699">***strand_mask_falloff***</span>
<br />An fCurve controlling the falloff of the mask from the edge of the strand.

<span style="color:#E69963">***use_object_falloff_for_strands***</span>
<br />When checked, this uses the same curve as the object mask.

<span style="color:#90A3F4">***render_material***</span>
<br />You can plug in an Arnold surface here.  If this is empty, a default "clay" material will be used for rendering.

<span style="color:#CCB699">***adjust_render_property_mask***</span>
<br />If a render property mask is connected, this allows adjustment of that mask.

<span style="color:#CCB699">***render_property_mask***</span>
<br />The render property mask is a scalar field that allows you to provide a "mask" that will be respected at render time or through the USD output.  This would allow a layered shader in Arnold using a AIGetUserData node for example.  It is output through the USD stage via vertex color alpha channel. 

<span style="color:#D9BE6C">***render_property_mask_property***</span>
<br />This is the property that will be passed to Arnold AIGetUserData via the mesh output at either resolution.

<span style="color:#E69963">***show_render_property_mask***</span>
<br />When checked, this will apply the render property mask as a colour of the low-res groundplane/custom object.

<span style="color:#E69963">***apply_step_curve***</span>
<br />If you want your displacement to step by a certain amount, check this on.

<span style="color:#A8D977">***step_curve***</span>
<br />Provides the stepping for the step mode.  The curve repeats before and after extrapolation, conforming the displacement to steps of a certain size and width that you can set by controlling the curve here.

***
## Output
<span style="color:#90A3F4">***display_out***</span>
<br />Low-res mesh output.  If this is being done on a custom mesh, this will be that mesh.

<span style="color:#90A3F4">***render_out***</span>
<br />High-res mesh output.  If this is being done on a custom mesh, this will be that mesh.

<span style="color:#CCB699">***weights***</span>
<br />The combined scalar field being used to weight the displacement.

<span style="color:#CCB699">***directions***</span>
<br />The combined vector field controlling the direction of the displacement.




