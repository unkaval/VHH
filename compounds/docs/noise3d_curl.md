### ***noise3d_curl***
<font size = 1>**Component Compound** - this compound is a component in the the *displacer* ecosystem.<br /><br /></font>
<font size = 2>**Curl Noise** - One of the pre-made fields.  This is the default curl noise field.</font><br />

***
## Input
<span style="color:#CCB699">***mask***</span>
<br />Scalar field mask on the outgoing field.

<span style="color:#CCB699">***warp_vector_field***</span>
<br />Domain warp on the outgoing field.

<span style="color:#82D99F">***field_weight***</span>
<br />Overall weight of this field from 0-1.

<span style="color:#82D99F">***magnitude***</span>
<br />Magnitude of the field.

<span style="color:#82D99F">***frequency***</span>
<br />Frequency of the field.

<span style="color:#CCB699">***time***</span>
<br />A scalar field with the time to sample the noise at. 

<span style="color:#62CFD9">***seed***</span>
<br />The seed to use for randomization.

<span style="color:#CCB699">***adjust_field***</span>
<br />An fCurve allowing you to adjust the field across values.

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
<span style="color:#CCB699">***curl_noise_field***</span>
<br />The field result ready to be used.

