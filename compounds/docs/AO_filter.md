### ***AO_filter***
<font size = 2>**Component Compound** - this compound is a component in the the *scatter plus* ecosystem.<br /><br /></font>
***Filter by Ambient Occlusion*** - One of the pre-made input filters.  This filters scatter weights by the ambient occlusion of the scatter mesh. <br />***Note:*** This is, by it's nature, extremely slow - use with caution.<br />

***
## Input
<span style="color:#E69963">***enable***</span>
<br />Enable or disable the filter.

<span style="color:#E69963">***reverse***</span>
<br />Flip the filtered weights.

<span style="color:#82D99F">***weight***</span>
<br />The weight of this filter in the stack.

<span style="color:#82D99F">***AO_brightness***</span>
<br />How much white to add to the unshadowed points.

<span style="color:#82D99F">***AO_radius***</span>
<br />The distance the AO rays will travel.

<span style="color:#62CFD9">***AO_resolution***</span>
<br />Hw many AO rays are generated per point.

<span style="color:#CCB699">***adjust_AO***</span>
<br />A curve adjustment of the AO output.

<span style="color:#E69963">***normalize_AO***</span>
<br />Remaps the output into a 0-1 range.

***
## Output
<span style="color:#90A3F4">***AO_filter_data***</span>
<br />The settings transported into Scatter Plus.

