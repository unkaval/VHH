### ***basic_road***
Ribbon generator, with banking, version 1.  No UVs yet<br />

***
## Input
<span style="color:#90A3F4">***strands***</span>
<br />Input strand for the road.  Resolution of this depends on the input, compound doesn't resample.

<span style="color:#82D99F">***sweep***</span>
<br />0 is no road, 1 is all the road.

<span style="color:#82D99F">***max_bank***</span>
<br />Maximum banking angle.

<span style="color:#82D99F">***width***</span>
<br />Width of the road.

<span style="color:#82D99F">***scale_uv***</span>
<br />The compound generates UVs **along the x-axis from 0 to 1** then uses the `width` input to height ratio to generate the y-axis values.  To evenly scale the UVs, use this setting.  

<span style="color:#E69963">***use_custom_UV_ratio***</span>
<br />As the compound uses the `width` input to height ratio to generate the UVs, when this is checked, you may enter your own ratio

<span style="color:#82D99F">***custom_width_ratio***</span>
<br />The width-to-height ratio you wish to use.

***
## Output
<span style="color:#82D99F">***out_mesh***</span>
<br />Road mesh output.

