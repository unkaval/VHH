### ***setup_strand_properties***
A compound for quickly setting up useful properties on an incoming strand.<br />

***
## Input
<span style="color:#90A3F4">***strands***</span>
<br />The incomign strand.

<span style="color:#E69963">***basis***</span>
<br />Generates point_normal, point_tangent, and point_binormal vectors for every point in the strand. These can be used to provide an orientation along the curve.

<span style="color:#E69963">***point_ratio***</span>
<br />Updates the strand with a normalised value of how far each point is along the curve, beginning at zero and ending at one.

<span style="color:#E69963">***curvature***</span>
<br />Updates the strand with a `point_curvature` property from 0 (least curvature) to 1 (most curvature).

<span style="color:#CCB699">&nbsp;&nbsp;&nbsp;***adjust_curvature***</span>
<br />&nbsp;&nbsp;&nbsp;An fCurve allowing you to adjust the resulting curvature.

<span style="color:#E69963">***length***</span>
<br />Updates the strand with a `point_length` and `strand_length` property.

***
## Output
<span style="color:#90A3F4">***out_strands***</span>
<br />Output strand with properties.

