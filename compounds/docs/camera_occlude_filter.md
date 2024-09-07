### ***camera_occlude_filter***
<font size = 2>**Component Compound** - this compound is a component in the the *scatter plus* ecosystem.<br /><br /></font>
***Filter by Camera Occlusion*** - One of the pre-made input filters.  This filters scatter weights based on the position and view direction of a camera.  Any points not seen by the camera will have zero weight.<br />

***
## Input
<span style="color:#E69963">***enable***</span>
<br />Enable or disable the filter.

<span style="color:#E69963">***reverse***</span>
<br />Flip the filtered weights.

<span style="color:#82D99F">***weight***</span>
<br />The weight of this filter in the stack.

<span style="color:#E67373">***camera_matrix***</span>
<br />The input world matrix fo the camera to occlude from.

***
## Output
<span style="color:#90A3F4">***camocc_filter_data***</span>
<br />The settings transported into Scatter Plus.

