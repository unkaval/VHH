### ***fresnel_viz***
Applies a fresnel effect to the vertex color.  The fresnel effect changes the colour of the vertex based on the incident angle to the camera. Requires a camera world matrix input.  Big thanks to [Ronja's tutorials.](https://www.ronja-tutorials.com/post/012-fresnel/)<br />

***
## Input
<span style="color:#90A3F4">***geo_input***</span>
<br />The geometry to visualize.

<span style="color:#E67373">***camera_world_matrix***</span>
<br />The selected camera's world matrix.

<span style="color:#E69963">***enable***</span>
<br />On/off switch.  If this is off, the object is passed through untouched.

<span style="color:#A8D977">***edge_color***</span>
<br />The colour at a grazing angle to the camera.

<span style="color:#A8D977">***center_color***</span>
<br />The colour at a direct angle to the camera.

<span style="color:#CCB699">***adjust_fresnel***</span>
<br />An fCurve used to modulate the transition from grazing to direct angles..

<span style="color:#82D99F">***transparency***</span>
<br />How transparent the geo display is. 0 = Opaque, 1 = transparent.

***
## Output
<span style="color:#CCB699">***geo_output***</span>
<br />The object.

