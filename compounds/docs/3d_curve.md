### ***noise3d_curve***
<font size = 1>**Component Compound** - this compound is a component in the the *displacer* ecosystem.<br /></font>
<font size = 2>This compound will produce a field based on the tangents of an input curve.  It is part of the *displacer* ecosystem, and as such, is one of the pre-made noises available for use.<br />This is a vector field for controlling the direction of the displacement.  This compound, like all the noise compounds can be masked by a ***scalar*** field and a domain warp can be provided by a ***vector*** field.</font><br />

***
## Input
<span style="color:#90A3F4">***curve_input***</span>
<br />This is the curve you are bringing in to use the tangents of.  This compound will check the curve for basis values and point_ratio, and if they are not coming in, with the curve, will calculate them.  If a curve is not connected to the compound, no desplacement directions will be applied.

<span style="color:#CCB699">***mask***</span>
<br />A ***scalar*** field, used to mask the **curve** field.

<span style="color:#CCB699">***warp_velocity_field***</span>
<br />A ***vector*** field, used to warp the domain of the **curve** field.

<span style="color:#82D99F">***field_weight***</span>
<br />Overall weight of this field from 0-1.

<span style="color:#CCB699">***adjust_curve***</span>
<br />This adjusts both the magnitude and the width of the curve displacement.  The Y-axis controls the magnitude and the X-axis controls the width.

<span style="color:#82D99F">***magnitude***</span>
<br />Overall magnitude of the outgoing field, negative values will reverse the direction of the field.

<span style="color:#82D99F">***curve_width***</span>
<br />The distance away from the curve that will be displaced.

<span style="color:#A8D977">***translation***</span>
<br />Translates the field in x, y and z axes.

<span style="color:#A8D977">***rotate***</span>
<br />Rotates the field in x, y and z axes.  This input is in degrees.

<span style="color:#A8D977">***scale***</span>
<br />Scales the field in x, y and z axes.

<span style="color:#82D99F">***warp_amount***</span>
<br />Warps the field with another field (domain warping).  If no field is connected to the warp input, this will do nothing.

<span style="color:#E69963">***invert_mask***</span>
<br />Inverts the connected mask field, if connected.

<span style="color:#CCB699">***adjust_mask***</span>
<br />Adjusts the connected mask field, if connected.

***
## Output
<span style="color:#CCB699">***curve_field***</span>
<br />The output vector field, ready to be connected to the *displacer* compound or used as a field in your graphs.

