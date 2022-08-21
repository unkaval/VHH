### ***vertical_stack***
This compound stacks meshes vertically, with various controls for size control, randomization, rotation etc.<br />

***
## Input
<span style="color:#90A3F4">***in_mesh***</span>
<br />This is your mesh to be stacked, the compound will make copies of this.

<span style="color:#62CFD9">***number_of_objects***</span>
<br />The number of objects in the stack.

<span style="color:#82D99F">***object_height_min***</span>
<br />Minimum height of the *stacked* object.

<span style="color:#82D99F">***object_height_max***</span>
<br />Maximum height of the *stacked* object.

<span style="color:#E69963">***reverse***</span>
<br />Reverses the direction of the stack.

<span style="color:#82D99F">***height_magnitude***</span>
<br />The overall vertical magnitude of the stack

<span style="color:#82D99F">***width_magnitude***</span>
<br />The overall horizontal magnitude of the stack.

<span style="color:#82D99F">***frequencies***</span>
<br />The number of frequencies in the randomization.

<span style="color:#82D99F">***master_frequency***</span>
<br />Frequency of the randomization.

<span style="color:#82D99F">***ratio***</span>
<br />Ratio of the randomization.

<span style="color:#82D99F">***frequency_ratio***</span>
<br />Frequency ratio of the randomization.

<span style="color:#62CFD9">***seed***</span>
<br />Ranomization seed.

<span style="color:#E69963">***random_scale_widths***</span>
<br />When checked, chooses a number of items in the stack that **might** get randomized.

<span style="color:#82D99F">***max_random_scaling_factor***</span>
<br />The maximum amount of scalaing, based on existing width.

<span style="color:#82D99F">***random_scale_chance***</span>
<br />The chance that each item will be scaled.  0 being no items, 1 being all items.

<span style="color:#62CFD9">***max_number_scaled***</span>
<br />The maximum number of randomly chosen items in the stack to be scaled.

<span style="color:#E69963">***offset_x_z***</span>
<br />Apply x/z offsets.

<span style="color:#82D99F">***max_offset***</span>
<br />Maximum amount of offset to apply.

<span style="color:#62CFD9">***offset_seed***</span>
<br />The seed for the random offsets.

<span style="color:#82D99F">***max_rotation***</span>
<br />The maximum radom rotation per item in the stack.

***
## Output
<span style="color:#82D99F">***out_stack***</span>
<br />The stack, output as a merged array.

