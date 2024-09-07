### ***steep_filter***
<font size = 2>**Component Compound** - this compound is a component in the the *scatter plus* ecosystem.<br /><br /></font>
***Filter Mesh Steepness*** - One of the pre-made input filters.  This filters scatter weights based on the angle of the normals of the scatter mesh.<br />

***
## Input
<span style="color:#E69963">***enable***</span>
<br />Enable or disable the filter.

<span style="color:#E69963">***reverse***</span>
<br />Flip the filtered weights.

<span style="color:#82D99F">***weight***</span>
<br />The weight of this filter in the stack.

<span style="color:#82D99F">***steep_threshold***</span>
<br />The angle above which weights will go to zero.

<span style="color:#CCB699">***adjust_falloff***</span>
<br />If *spread* is above zero, this will adjust the falloff of the spread.

<span style="color:#82D99F">***spread***</span>
<br />how much the threshold spreads, higher numbers will make a softer threshold.


***
## Output
<span style="color:#90A3F4">***steep_filter_data***</span>
<br />The settings transported into Scatter Plus.

