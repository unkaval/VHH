### ***curvature_filter***
<font size = 2>**Component Compound** - this compound is a component in the the *scatter plus* ecosystem.<br /><br /></font>
***Filter by Curvature*** - One of the pre-made input filters.  This filters scatter weights based on the curvature values of the input mesh.<br />

***
## Input
<span style="color:#E69963">***enable***</span>
<br />Enable or disable the filter.

<span style="color:#E69963">***reverse***</span>
<br />Flip the filtered weights.

<span style="color:#82D99F">***weight***</span>
<br />The weight of this filter in the stack.

<span style="color:#CCB699">***adjust_curvature***</span>
<br />A curve used to adjust the curvature.

<span style="color:#62CFD9">***blur_iterations***</span>
<br />The curvature property can be blurred.  This is the number of iterations in the blur loop.

<span style="color:#E69963">***exclude_edges***</span>
<br />An edge is a harsh curvature, this will exclude the edges of the scatter mesh.

***
## Output
<span style="color:#90A3F4">***curvature_filter_data***</span>
<br />The settings transported into Scatter Plus.

