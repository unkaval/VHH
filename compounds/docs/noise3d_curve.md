### ***noise3d_curve***
<font size = 1>**Component Compound** - this compound is a component in the the *displacer* ecosystem.<br /><br /></font>
<font size = 2>**Curve Displace** - One of the pre-made fields.  This displace ther directions of the field based on a strand input</font><br />

***
## Input
<span style="color:#90A3F4">***curve_input***</span>
<br />This is the curve you are bringing in to use the tangents of.  This compound will check the curve for basis values and point_ratio, and if they are not coming in, with the curve, will calculate them.  If a curve is not connected to the compound, no desplacement directions will be applied.

<span style="color:#CCB699">***mask***</span>
<br />Scalar field mask on the outgoing field.

<span style="color:#CCB699">***warp_vector_field***</span>
<br />Domain warp on the outgoing field.

<span style="color:#82D99F">***field_weight***</span>
<br />Overall weight of this field from 0-1.

<span style="color:#A8D977">***adjust_curve***</span>
<br />This adjusts both the magnitude and the width of the curve displacement.  The Y-axis controls the magnitude and the X-axis controls the width.

<span style="color:#82D99F">***magnitude***</span>
<br />Overall magnitude of the outgoing field, negative values will reverse the direction of the field.

<span style="color:#82D99F">***curve_width***</span>
<br />Minimum width to displace away from the curve.

<span style="color:#CCB699">***adjust_field***</span>
<br />An fCurve allowing you to adjust the field across values.

<span style="color:#62CFD9">***displace_direction***</span>
<br />The curve can be used to displace along it's tangent or binormal.

<span style="color:#A8D977">***translate***</span>
<br />Move the field.

<span style="color:#A8D977">***rotate***</span>
<br />Rotate the field.

<span style="color:#A8D977">***scale***</span>
<br />Scale the field.

<span style="color:#82D99F">***warp_amount***</span>
<br />The amount to warp the field based on the field used as a domain warp.

<span style="color:#E69963">***invert_mask***</span>
<br />Inverts the scalar field mask.

<span style="color:#CCB699">***adjust_mask***</span>
<br />A curve input that adjusts the scalar field mask.

***
## Output
<span style="color:#CCB699">***curve_field***</span>
<br />The field result ready to be used.

