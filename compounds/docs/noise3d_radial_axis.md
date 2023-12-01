### ***noise3d_radial_axis***
<font size = 1>**Component Compound** - this compound is a component in the the *displacer* ecosystem.<br /><br /></font>
<font size = 2>**Radial Axis** - One of the pre-made fields.  This will generate a vector field that revolves around an axis.</font><br />


***
## Input
<span style="color:#CCB699">***mask***</span>
<br />Scalar field mask on the outgoing field.

<span style="color:#CCB699">***warp_vector_field***</span>
<br />Domain warp on the outgoing field.

<span style="color:#82D99F">***field_weight***</span>
<br />Overall weight of this field from 0-1.

<span style="color:#A8D977">***axis***</span>
<br />The axis you will be rotating around.

<span style="color:#A8D977">***modulate_field***</span>
<br />The strength of the field, from the center out.

<span style="color:#82D99F">***amplitude***</span>
<br />The amplitude of the field.

<span style="color:#CCB699">***adjust_field***</span>
<br />An fCurve allowing you to adjust the field across values.

<span style="color:#82D99F">***magnitude***</span>
<br />Magnitude of the noise field.

<span style="color:#82D99F">***num_frequencies***</span>
<br />This is the total number of noise frequencies to sum. Generally as this number increases there will be more detail or small scale noise. The value does not need to be an integer.

<span style="color:#82D99F">***frequency***</span>
<br />This is the base frequency of the fractal noise. Higher values have finer detail.

<span style="color:#82D99F">***ratio***</span>
<br />This is the ratio of magnitude of each noise frequency to the previous. If it is the same as frequency_ratio then the magnitude of each noise will be the same relative to its scale.

<span style="color:#82D99F">***frequency_ratio***</span>
<br />This is the ratio of each noise frequency to the previous.

<span style="color:#CCB699">***time***</span>
<br />A scalar field with the time to sample the noise at. 

<span style="color:#62CFD9">***seed***</span>
<br />Seed for the random number generator.

<span style="color:#A8D977">***translate***</span>
<br />Move the field.

<span style="color:#A8D977">***rotate***</span>
<br />Rotate the field.

<span style="color:#A8D977">***scale***</span>
<br />Scale the field.

<span style="color:#E69963">***invert_mask***</span>
<br />Inverts the scalar field mask.

<span style="color:#CCB699">***adjust_mask***</span>
<br />A curve input that adjusts the scalar field mask.

<span style="color:#82D99F">***warp_amount***</span>
<br />The amount to warp the field based on the field used as a domain warp.


***
## Output
<span style="color:#CCB699">***radial_axis_field***</span>
<br />The field result ready to be used.

