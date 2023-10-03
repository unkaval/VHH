### ***noise3d_radial_axis***
<font size = 1>**Component Compound** - this compound is a component in the the *displacer* ecosystem.<br /></font>
<font size = 2>This compound will produce a radial axis field, a circular field around a given axis.  It is part of the *displacer* ecosystem, and as such, is one of the pre-made noises available for use.<br />This is a vector field for controlling the direction of the displacement.  This compound, like all the noise compounds can be masked by a ***scalar*** field and a domain warp can be provided by a ***vector*** field.</font><br />

***
## Input
<span style="color:#CCB699">***mask_in***</span>
<br />Description.

<span style="color:#CCB699">***warp_vector_field***</span>
<br />Description.

<span style="color:#A8D977">***axis***</span>
<br />This is the axis around which the field rotates.

<span style="color:#CCB699">***modulate_field***</span>
<br />An fCurve that controsl the strength of the field from the axis outwards.

<span style="color:#82D99F">***amplitude***</span>
<br />The master amplitude of the field.

<span style="color:#82D99F">***magnitude***</span>
<br />The radial field allows you to add noise, this is the magnitude of that noise.

<span style="color:#82D99F">***num_frequencies***</span>
<br />Number of frequencies in the added noise field.

<span style="color:#82D99F">***frequency***</span>
<br />The frequency of the added noise field.

<span style="color:#82D99F">***ratio***</span>
<br />The ratio of the added noise field.

<span style="color:#82D99F">***frequency_ratio***</span>
<br />The frequency ratio of the added noise field.

<span style="color:#CCB699">***time***</span>
<br />Connect a time node to evolve the added field.

<span style="color:#62CFD9">***seed***</span>
<br />The seed of the added noise field.

<span style="color:#A8D977">***translate***</span>
<br />Translates the field in x, y and z axes.

<span style="color:#A8D977">***rotate***</span>
<br />Rotates the field in x, y and z axes.  This input is in degrees.

<span style="color:#A8D977">***scale***</span>
<br />Scales the field in x, y and z axes.

<span style="color:#E69963">***invert_mask***</span>
<br />Inverts the connected mask field, if connected.

<span style="color:#CCB699">***adjust_mask***</span>
<br />Adjusts the connected mask field, if connected.

<span style="color:#82D99F">***warp_amount***</span>
<br />Warps the field with another field (domain warping).  If no field is connected to the warp input, this will do nothing.

***
## Output
<span style="color:#CCB699">***radial_axis_field***</span>
<br />The output vector field, ready to be connected to the *displacer* compound or used as a field in your graphs.

