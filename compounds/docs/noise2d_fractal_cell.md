### ***noise2d_fractal_cell***
<font size = 1>**Component Compound** - this compound is a component in the the *displacer* ecosystem.<br /><br /></font>
<font size = 2>**Sine** - One of the pre-made fields.  This is a cellular field with an inbuild FBM system, letting you have levels of noise..</font><br />


***
## Input
<span style="color:#CCB699">***mask***</span>
<br />Scalar field mask on the outgoing field.

<span style="color:#CCB699">***warp_vector_field***</span>
<br />Domain warp on the outgoing field.

<span style="color:#82D99F">***field_weight***</span>
<br />Overall weight of this field from 0-1.

<span style="color:#62CFD9">***octaves***</span>
<br />This is the total number of noise frequencies to sum. Generally as this number increases there will be more detail or small scale noise. The value IS an integer.

<span style="color:#82D99F">***frequency***</span>
<br />This is the base frequency of the fractal noise. Higher values have finer detail.

<span style="color:#82D99F">***magnitude***</span>
<br />The magnitude of the noise.

<span style="color:#82D99F">***randomosity***</span>
<br />How random the cells are.

<span style="color:#62CFD9">***seed***</span>
<br />The seed to use for randomization.

<span style="color:#A8D977">***weight_per_octave***</span>
<br />An fCurve ascribing weight to the octaves, low-frequecy on the left, high frequency on the right.

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

<span style="color:#E69963">***step_field***</span>
<br />When this is selected, the field is discretized into "steps".

<span style="color:#CCB699">***step_shape***</span>
<br />The shape of the steps.  Because the curve pre- and post-extrapolation is set to "Relative Repeat" this acts like a modulo on the field.  You can vary the shape of your stepping with just the controls on this curve.

<span style="color:#CCB699">***step_mask***</span>
<br />A scalar field input to mask area of the step field.

<span style="color:#E69963">***invert_step_mask***</span>
<br />When this is checked, the step_mask is inverted.

<span style="color:#CCB699">***adjust_step_mask***</span>
<br />An fCurve allowing adjustment of the step_mask.

***
## Output
<span style="color:#CCB699">***fractal_cell_field***</span>
<br />Description.

