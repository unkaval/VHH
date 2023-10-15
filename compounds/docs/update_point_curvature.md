### ***update_point_curvature***
This compound uses vertex-to-edge average calculations to return a curvature value between 0 and 1.  It works on strands and meshes while all other data types are passed through unchanged..<br />

***
## Input
<span style="color:#90A3F4">***input***</span>
<br />The Object you wish to calculated the curvature of.

<span style="color:#A8D977">***adjust_curvature***</span>
<br />An fCurve allowing you to adjust the output curvature.

***
## Output
<span style="color:#90A3F4">***output_with_curvature***</span>
<br />The object is output with a `point_curvature` geo property.

<span style="color:#D9BE6C">***property***</span>
<br />String name of the output property for ease of connection.

